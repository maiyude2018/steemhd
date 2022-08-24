### 本工具支持：
- 从助记词或私钥，按hdwallet的规则生成多链地址
- 计算steem公私钥的工具
- 支持把steem的公钥按照hdwallet的规则转换为其他链的地址

### INSTALL
pip install steemhd

#### 目前支持的地址转换
 - STEEM <==> ETH 
 - STEEM <==> TRON
 - STEEM <==> COSMOS
 - ETH <==> EVMOS
 - ETH <==> TRON
 - TRON <==> ETH
 
 ### 目前支持生成地址的链
 - STEEM
 - BTC
 - DOGE
 - ETH
 - TRON
 - EVMOS
 - COSMOS
 - TERRA
 - 大部分cosmos系的链

#### 使用示例

````
import steemhd.teem_to_hdwallet as sd


#从密码计算所有公私钥对
account="maiyude"
passwd="helloworld"
keys=sd.get_key_steem(account,passwd)
print(keys)

#从steem私钥获得公钥
key="5JaRW6KRjMqj5bxCQAn37zZg76bDfoteSwZvP64j1ApSZaFtmKs"
stm=sd.get_pubkey(key)
print(stm)

#从steem公钥获得对应eth地址
stm="STM7UpXLm8WGaBWZmcnCYD88zesBoXhGR6eV5HP6tKxtpmRhPfSit"
eth_addr=sd.get_eth_addr_fromsteem(stm)
print(eth_addr)

#从steem公钥获得对应tron地址
stm="STM7UpXLm8WGaBWZmcnCYD88zesBoXhGR6eV5HP6tKxtpmRhPfSit"
tron_addr=sd.get_tron_addr_fromsteem(stm)
print(tron_addr)

#从steem公钥获得对应cosmos地址
stm="STM7UpXLm8WGaBWZmcnCYD88zesBoXhGR6eV5HP6tKxtpmRhPfSit"
cosmos_addr=sd.get_cosmos_addr_fromsteem(stm)
print(cosmos_addr)

#从steem私钥获得对应eth私钥
pri_key="5KLWLNT3v1s4tLKFYjrFb1hVpHFZkcA6syrNhapFU35DPd1ML6m"
eth_key=sd.get_eth_privkey(pri_key)
print("eth_key",eth_key)

#从steem私钥获得对应btc私钥
pri_key="5KLWLNT3v1s4tLKFYjrFb1hVpHFZkcA6syrNhapFU35DPd1ML6m"
btc_key=sd.get_btc_privkey(pri_key)
print("btc_key1",btc_key)

#从eth私钥获得对应steem私钥
privkey="c85064d7c3cba0fd71ea98e438899b579227a87bd1d9316503ef2dd2689294f7"
steem_key=sd.get_steem_privkey(privkey)
print("steem_key",steem_key)

#私钥转WIF(BTC)
privkey="c85064d7c3cba0fd71ea98e438899b579227a87bd1d9316503ef2dd2689294f7"
btc_key=sd.privkey_towif(0x80,privkey,"01")
print("btc_key2",btc_key)

#私钥转WIF(DOGE)
privkey="2542b1a3e16398a3860543e6343601518b97f2e94ed4fa1fdbe27d9096599077"
doge_key=sd.privkey_towif(0x9e,privkey,"01")
print("DOGE",doge_key)

#wif转raw_key
wif="L3w6UVfyrzoz9aFZD68PP85kBgjHZUBAx1vvn8FYrL9bgVRCyjhf"
btc_raw_key=sd.get_eth_privkey(wif)[:-2]
print("btc_raw_key",btc_raw_key)

#从ETH地址得到evmos地址
raw_address="0xdd96de0d29092cbbf11d4739ec0d440752bdd307"
evmos_addr=sd.eth_to_bech32(raw_address, prefix="evmos")
print(evmos_addr)

#从ETH地址获得对应tron地址
raw_address="0xdd96de0d29092cbbf11d4739ec0d440752bdd307"
tron_addr = sd.eth_to_tron(raw_address)
print(tron_addr)

#从tron地址获得对应eth地址
raw_address="TWAs4uMQ1bVxksLdoCwkvgCZbqwLM6ScR2"
eth_addr = sd.tron_to_eth(raw_address)
print(eth_addr)

#获得某个用户公钥对应的eth地址
eth_addr_accounts=sd.get_eth_addr_accounts("maiyude")
print(eth_addr_accounts)

````


#### 生成多链地址使用示例
````
from steemhd.pyhd import hd_wallet_CreateFromMnemonic,hd_wallet_CreateFromprivatekey,steem_wallet_CreateFromMnemonic,btc_pub_to_addr

BTC_DERIVATION_PATH = "m/44'/0'/0'/0"
DOGE_DERIVATION_PATH = "m/44'/3'/0'/0"
ETH_DERIVATION_PATH = "m/44'/60'/0'/0"
COSMOS_DERIVATION_PATH = "m/44'/118'/0'/0"
TRON_DERIVATION_PATH = "m/44'/195'/0'/0"



mnemonics = "horn bonus still lobster exclude submit minimum above soap pilot antenna humble memory crew tooth exotic rich seek nominee cupboard sunny shine pause custom"


#BTC
addr_num=0
coins="BTC"
print(coins)
PATH=BTC_DERIVATION_PATH
wallet=hd_wallet_CreateFromMnemonic(mnemonics,PATH,addr_num,coins)
print(wallet,"\n")
private_key = "L1oFfZnoHtSDKP55p2p28AKb3yCnWJG7Rgc1fR1fXAMb4YiVuWvJ"
wallet=hd_wallet_CreateFromprivatekey(private_key,coins)
print(wallet)
print("----------------------------------------------------\n")

#DOGE
coins="DOGE"
print(coins)
wallet=hd_wallet_CreateFromMnemonic(mnemonics,DOGE_DERIVATION_PATH,0,coins)
print(wallet,"\n")
private_key = "QPs4FdgThuAUNzXkpehyFCd8awPBmrUfM8d7NYePWgUVusttBTky"
wallet=hd_wallet_CreateFromprivatekey(private_key,coins)
print(wallet)
print("----------------------------------------------------\n")

#ETH
addr_num=0
coins="ETH"
print(coins)
PATH=ETH_DERIVATION_PATH
wallet=hd_wallet_CreateFromMnemonic(mnemonics,PATH,addr_num,coins)
print(wallet,"\n")
private_key = "c85064d7c3cba0fd71ea98e438899b579227a87bd1d9316503ef2dd2689294f7"
wallet=hd_wallet_CreateFromprivatekey(private_key,coins)
print(wallet)
print("----------------------------------------------------\n")

#TRON
coins="TRON"
print(coins)
PATH=TRON_DERIVATION_PATH
wallet=hd_wallet_CreateFromMnemonic(mnemonics,PATH,addr_num,coins)
print(wallet,"\n")
private_key = "29efb52958f443e522fe52b89856c601c41b8910a0ef1d7f8b9beb2f11a8e684"
wallet=hd_wallet_CreateFromprivatekey(private_key,coins)
print(wallet)
print("----------------------------------------------------\n")

#COSMOS
coins="COSMOS"
print(coins)
PATH=COSMOS_DERIVATION_PATH
wallet=hd_wallet_CreateFromMnemonic(mnemonics,PATH,addr_num,coins)
print(wallet,"\n")
private_key = "1f9d07b9ca4f99a0949302c428cefe67c90fc16ab53c3776e5f660a2dbb2e8f3"
wallet=hd_wallet_CreateFromprivatekey(private_key,coins)
print(wallet)
print("----------------------------------------------------\n")

#EVMOS
addr_num=0
coins="EVMOS"
print(coins)
PATH=ETH_DERIVATION_PATH
wallet=hd_wallet_CreateFromMnemonic(mnemonics,PATH,addr_num,coins)
print(wallet,"\n")
private_key = "2c34e1161d70404fd5d8ae29d1c15cfb36b6e1d4c0134b25c8edd6f7a87c35d6"
wallet=hd_wallet_CreateFromprivatekey(private_key,coins)
print(wallet)
print("----------------------------------------------------\n")

#STEEM
coins="STEEM"
print(coins)
wallet=steem_wallet_CreateFromMnemonic(mnemonics)
print(wallet,"\n")
private_key = "4ab17289b2739c5500848fd10bd2df03a46575795792fe53e36764f056c8d4e9"
wallet=hd_wallet_CreateFromprivatekey(private_key,coins)
print(wallet)
print("----------------------------------------------------\n")

#COSMOS系，hdpath = "m/44'/118'/0'/0"的链
#例AKASH,格式：COSMOS_AKASH
coins="COSMOS_TERRA"
print(coins)
PATH=COSMOS_DERIVATION_PATH
wallet=hd_wallet_CreateFromMnemonic(mnemonics,PATH,addr_num,coins)
print(wallet,"\n")
private_key = "1f9d07b9ca4f99a0949302c428cefe67c90fc16ab53c3776e5f660a2dbb2e8f3"
wallet=hd_wallet_CreateFromprivatekey(private_key,coins)
print(wallet)
print("----------------------------------------------------\n")

coins="COSMOS_IDEP"
print(coins)
PATH=COSMOS_DERIVATION_PATH
wallet=hd_wallet_CreateFromMnemonic(mnemonics,PATH,addr_num,coins)
print(wallet,"\n")


````

