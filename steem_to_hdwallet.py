import hashlib
from base58_utils.base58_steem import Base58,gphBase58CheckEncode,base58CheckEncode,gphBase58CheckDecode,base58CheckDecode
from base58_utils.base58_tron import Base58ChecksumError, Base58Decoder, Base58Encoder
from base58_utils.bech32_ex import Bech32ChecksumError
from base58_utils.bech32 import Bech32Decoder, Bech32Encoder
from base58_utils.cypto import CryptoUtils
from binascii import hexlify, unhexlify
import ecdsa
from Crypto.Hash import keccak
import requests


#从steem私钥获得对应eth私钥
def get_eth_privkey(wif):
    return base58CheckDecode(wif)


#从steem私钥获得公钥
def get_pubkey(wif):
    """ Derive uncompressed public key """
    privkey = Base58(wif)
    secret = unhexlify(repr(privkey))
    order = ecdsa.SigningKey.from_string(secret, curve=ecdsa.SECP256k1).curve.generator.order()
    p = ecdsa.SigningKey.from_string(secret, curve=ecdsa.SECP256k1).verifying_key.pubkey.point
    x_str = ecdsa.util.number_to_string(p.x(), order)
    # y_str = ecdsa.util.number_to_string(p.y(), order)
    compressed = hexlify(chr(2 + (p.y() & 1)).encode("ascii") + x_str).decode("ascii")
    # uncompressed = hexlify(
    #    chr(4).encode('ascii') + x_str + y_str).decode('ascii')
    return "STM"+gphBase58CheckEncode(compressed)


#从密码计算所有公私钥对
def get_key_steem(account,passwd):
    keys=[]
    role = ["owner","posting","active","memo"]
    for i in role:
        seed = account + i + passwd
        seed_bytes = bytes(seed, 'utf-8')
        s = hashlib.sha256(seed_bytes).digest()
        raw_pri = hexlify(s).decode('ascii')
        key = base58CheckEncode(0x80, raw_pri)
        keys.append(key)
    json={"account":account,"passwd":passwd,
          "owner_key": {"private": keys[0], "public": get_pubkey(keys[0])},
          "posting_key": {"private": keys[1], "public": get_pubkey(keys[1])},
          "active_key": {"private": keys[2], "public": get_pubkey(keys[2])},
          "memo_key": {"private": keys[3], "public": get_pubkey(keys[3])}
          }
    return json


def pow_mod(x, y, z):
    "Calculate (x ** y) % z efficiently"
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number

#从compressed_key获得uncompressed_key
def get_uncompressed_key(compressed_key):
    Pcurve = 2 ** 256 - 2 ** 32 - 2 ** 9 - 2 ** 8 - 2 ** 7 - 2 ** 6 - 2 ** 4 - 1

    y_parity = int(compressed_key[:2]) - 2
    x = int(compressed_key[2:], 16)

    a = (pow_mod(x, 3, Pcurve) + 7) % Pcurve

    y = pow_mod(a, (Pcurve + 1) // 4, Pcurve)

    if y % 2 != y_parity:
        y = -y % Pcurve
    uncompressed_key = '04{:x}{:x}'.format(x, y)
    return uncompressed_key

#从uncompressed_key获得eth地址
def get_eth_addr(uncompressed_key):
    keccak_hash = keccak.new(digest_bits=256)
    public_key = uncompressed_key[2:]
    public_key = bytes.fromhex(public_key)
    keccak_hash.update(public_key)
    addr = "0x" + keccak_hash.hexdigest()[-40:]
    return addr

#从steem公钥获得对应eth地址
def get_eth_addr_fromsteem(addr_steem):
    s = addr_steem.replace("STM", "")
    raw_compr_pub = gphBase58CheckDecode(s)
    uncompressed_key = get_uncompressed_key(raw_compr_pub)
    address = get_eth_addr(uncompressed_key)
    return address

#从steem公钥获得对应tron地址
def get_tron_addr_fromsteem(addr_steem):
    s = addr_steem.replace("STM", "")
    raw_compr_pub = gphBase58CheckDecode(s)
    uncompressed_key = get_uncompressed_key(raw_compr_pub)
    address = get_eth_addr(uncompressed_key)
    addr = address.replace("0x", "")
    addrs = Base58Encoder.CheckEncode(b"\x41" + bytes.fromhex(addr))
    return addrs

#从steem公钥获得对应cosmos地址
def get_cosmos_addr_fromsteem(addr_steem):
    s = addr_steem.replace("STM", "")
    raw_compr_pub = gphBase58CheckDecode(s)
    addrs = Bech32Encoder.Encode("cosmos", CryptoUtils.Hash160(bytes.fromhex(raw_compr_pub)))
    return addrs

#获得某个用户公钥对应的eth地址
def get_eth_addr_accounts(accounts):
    nodes = 'https://api.justyy.com'
    data = {"jsonrpc": "2.0", "method": "condenser_api.get_accounts", "params": [[accounts]], "id": 1}
    r = requests.post(nodes, json=data)
    rjson = r.json()["result"]
    owner = rjson[0]["owner"]["key_auths"][0][0]
    posting = rjson[0]["posting"]["key_auths"][0][0]
    active = rjson[0]["active"]["key_auths"][0][0]
    addrs={"account":accounts,
           "owner":get_eth_addr_fromsteem(owner),
           "posting":get_eth_addr_fromsteem(posting),
           "active":get_eth_addr_fromsteem(active)}
    return addrs


