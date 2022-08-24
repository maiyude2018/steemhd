#!/usr/bin/env python3
'''
MIT License

Copyright (c) 2018 Luis Teixeira
Copyright (c) 2019 Niklas Baumstark

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
import binascii, hashlib, hmac, struct
from ecdsa.curves import SECP256k1
from eth_utils import to_checksum_address, keccak as eth_utils_keccak
import steemhd.steem_to_hdwallet as sd
import codecs
import ecdsa
import base58

BIP39_PBKDF2_ROUNDS = 2048
BIP39_SALT_MODIFIER = "mnemonic"
BIP32_PRIVDEV = 0x80000000
BIP32_CURVE = SECP256k1
BIP32_SEED_MODIFIER = b'Bitcoin seed'
ETH_DERIVATION_PATH = "m/44'/60'/0'/0"
COSMOS_DERIVATION_PATH = "m/44'/118'/0'/0"
TRON_DERIVATION_PATH = "m/44'/195'/0'/0"
COSMOS_BECH32_HRP = "cosmos"


class PublicKey:
    def __init__(self, private_key):
        self.point = int.from_bytes(private_key, byteorder='big') * BIP32_CURVE.generator

    def __bytes__(self):
        xstr = self.point.x().to_bytes(32, byteorder='big')
        parity = self.point.y() & 1
        pub=(2 + parity).to_bytes(1, byteorder='big') + xstr
        return pub

    def uncompr_pub(self):
        x = self.point.x()
        y = self.point.y()
        s = x.to_bytes(32, 'big') + y.to_bytes(32, 'big')
        uncompr_pub = '04' + binascii.hexlify(s).decode("utf-8")
        return uncompr_pub

    def address(self):
        x = self.point.x()
        y = self.point.y()
        s = x.to_bytes(32, 'big') + y.to_bytes(32, 'big')

        return to_checksum_address(eth_utils_keccak(s)[12:])


def mnemonic_to_bip39seed(mnemonic, passphrase):
    mnemonic = bytes(mnemonic, 'utf8')
    salt = bytes(BIP39_SALT_MODIFIER + passphrase, 'utf8')
    return hashlib.pbkdf2_hmac('sha512', mnemonic, salt, BIP39_PBKDF2_ROUNDS)


def bip39seed_to_bip32masternode(seed):
    k = seed
    h = hmac.new(BIP32_SEED_MODIFIER, seed, hashlib.sha512).digest()
    key, chain_code = h[:32], h[32:]
    return key, chain_code


def derive_bip32childkey(parent_key, parent_chain_code, i):
    assert len(parent_key) == 32
    assert len(parent_chain_code) == 32
    k = parent_chain_code
    if (i & BIP32_PRIVDEV) != 0:
        key = b'\x00' + parent_key
    else:
        key = bytes(PublicKey(parent_key))
    d = key + struct.pack('>L', i)
    while True:
        h = hmac.new(k, d, hashlib.sha512).digest()
        key, chain_code = h[:32], h[32:]
        a = int.from_bytes(key, byteorder='big')
        b = int.from_bytes(parent_key, byteorder='big')
        key = (a + b) % BIP32_CURVE.order
        if a < BIP32_CURVE.order and key != 0:
            key = key.to_bytes(32, byteorder='big')
            break
        d = b'\x01' + h[32:] + struct.pack('>L', i)
    return key, chain_code


def parse_derivation_path(str_derivation_path):
    path = []
    if str_derivation_path[0:2] != 'm/':
        raise ValueError("Can't recognize derivation path. It should look like \"m/44'/60/0'/0\".")
    for i in str_derivation_path.lstrip('m/').split('/'):
        if "'" in i:
            path.append(BIP32_PRIVDEV + int(i[:-1]))
        else:
            path.append(int(i))
    return path


def mnemonic_to_private_key(mnemonic, str_derivation_path, passphrase=""):
    derivation_path = parse_derivation_path(str_derivation_path)
    bip39seed = mnemonic_to_bip39seed(mnemonic, passphrase)
    master_private_key, master_chain_code = bip39seed_to_bip32masternode(bip39seed)
    private_key, chain_code = master_private_key, master_chain_code
    for i in derivation_path:
        #print("private_key",binascii.hexlify(bytes(private_key)).decode("utf-8"))
        private_key, chain_code = derive_bip32childkey(private_key, chain_code, i)
    return bip39seed,private_key,master_private_key

def __private_to_public(private_key):
    private_key_bytes = codecs.decode(private_key, 'hex')
    # Get ECDSA public key
    key = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1).verifying_key
    key_bytes = key.to_string()
    public_key = codecs.encode(key_bytes, 'hex')
    return public_key



def hd_wallet_CreateFromMnemonic(mnemonics,hdpath,addr_num,coins):
    seed_bytes, private_key, master_private_key = mnemonic_to_private_key(mnemonics,str_derivation_path=f'{hdpath}/%s' % str(addr_num))
    public_key = PublicKey(private_key)
    private_key=binascii.hexlify(private_key).decode("utf-8")
    if coins == "ETH":
        address = public_key.address()
    elif coins == "BTC":
        address = btc_pub_to_addr("00", binascii.hexlify(bytes(public_key)).decode("utf-8"))
    elif coins == "DOGE":
        address = btc_pub_to_addr("1e", binascii.hexlify(bytes(public_key)).decode("utf-8"))
    elif coins == "TRON":
        address = sd.eth_to_tron(public_key.address())
    elif "COSMOS" in coins:
        if coins == "COSMOS":
            address = sd.get_cosmosaddr_frompubkey("cosmos",binascii.hexlify(bytes(public_key)).decode("utf-8"))
        else:
            coins=coins.replace("COSMOS_","")
            address = sd.get_cosmosaddr_frompubkey(coins.lower(), binascii.hexlify(bytes(public_key)).decode("utf-8"))
    elif coins == "EVMOS":
        address = [public_key.address(),sd.eth_to_bech32(public_key.address(), prefix="evmos")]
    elif coins == "STEEM":
        private_key = sd.get_steem_privkey(private_key)
        address = sd.get_pubkey(private_key)
    else:
        address = None
    json={"mnemonics":mnemonics,
          "seed_bytes":binascii.hexlify(bytes(seed_bytes)).decode("utf-8"),
          "master_private_key":binascii.hexlify(bytes(master_private_key)).decode("utf-8"),
          "public_key":binascii.hexlify(bytes(public_key)).decode("utf-8"),
          "uncompr_pubkey":public_key.uncompr_pub(),
          "privkey":private_key,
          "address":address
          }
    if coins == "BTC" or coins == "DOGE":
        wif=sd.privkey_towif(0x9e, json["privkey"], '01')
        json.update({"wif_privkey":wif})
    return json

def steem_wallet_CreateFromMnemonic(mnemonics,hdpath="m/44'/60'/0'/0"):
    owner=hd_wallet_CreateFromMnemonic(mnemonics,hdpath,0,"STEEM")
    posting=hd_wallet_CreateFromMnemonic(mnemonics,hdpath,1,"STEEM")
    active=hd_wallet_CreateFromMnemonic(mnemonics,hdpath,2,"STEEM")
    memo=hd_wallet_CreateFromMnemonic(mnemonics,hdpath,3,"STEEM")
    key={
        "owner_key": {"private": owner["privkey"], "public": owner["address"]},
          "posting_key": {"private": posting["privkey"], "public": posting["address"]},
          "active_key": {"private": active["privkey"], "public": active["address"]},
          "memo_key": {"private": memo["privkey"], "public": memo["address"]}
    }
    json = {"mnemonics": owner["mnemonics"],
            "seed_bytes": owner["seed_bytes"],
            "master_private_key": owner["master_private_key"],
            "keys": key
            }
    return json


def btc_pub_to_addr(network,ecdsaPublicKey):
    hash256FromECDSAPublicKey = hashlib.sha256(binascii.unhexlify(ecdsaPublicKey)).hexdigest()
    ridemp160FromHash256 = hashlib.new('ripemd160', binascii.unhexlify(hash256FromECDSAPublicKey))
    prependNetworkByte = network + ridemp160FromHash256.hexdigest()
    hash = prependNetworkByte
    for x in range(1, 3):
        hash = hashlib.sha256(binascii.unhexlify(hash)).hexdigest()
    cheksum = hash[:8]
    appendChecksum = prependNetworkByte + cheksum
    bitcoinAddress = base58.b58encode(binascii.unhexlify(appendChecksum))
    return bitcoinAddress.decode('utf8')


def hd_wallet_CreateFromprivatekey(private_key,coins):
    # private_key to Eth address
    if coins == "BTC" or coins == "DOGE":
        wif = private_key
        private_key = sd.get_eth_privkey(private_key)[:-2]
    privkey = bytes.fromhex(private_key)
    public_key = PublicKey(privkey)
    if coins == "ETH":
        address = public_key.address()
    elif coins == "BTC":
        address = btc_pub_to_addr("00", binascii.hexlify(bytes(public_key)).decode("utf-8"))
    elif coins == "DOGE":
        address = btc_pub_to_addr("1e", binascii.hexlify(bytes(public_key)).decode("utf-8"))
    elif coins == "TRON":
        address = sd.eth_to_tron(public_key.address())
    elif "COSMOS" in coins:
        if coins == "COSMOS":
            address = sd.get_cosmosaddr_frompubkey("cosmos", binascii.hexlify(bytes(public_key)).decode("utf-8"))
        else:
            coins = coins.replace("COSMOS_", "")
            address = sd.get_cosmosaddr_frompubkey(coins.lower(), binascii.hexlify(bytes(public_key)).decode("utf-8"))
    elif coins == "EVMOS":
        address = [public_key.address(),sd.eth_to_bech32(public_key.address(), prefix="evmos")]
    elif coins == "STEEM":
        private_key = sd.get_steem_privkey(private_key)
        address = sd.get_pubkey(private_key)
    else:
        address = None
    json={"public_key":binascii.hexlify(bytes(public_key)).decode("utf-8"),
          "uncompr_pubkey":public_key.uncompr_pub(),
          "privkey":private_key,
          "address":address
          }
    if coins == "BTC" or coins == "DOGE":
        json.update({"wif_privkey":wif})
    return json