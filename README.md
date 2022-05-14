### 本工具支持：
- 从助记词或私钥，按hdwallet的规则生成多链地址
- 计算steem公私钥的工具
- 支持把steem的公钥按照hdwallet的规则转换为其他链的地址

#### 目前支持的地址转换
 - STEEM to ETH
 - STEEM to TRON
 - STEEM to COSMOS
 - ETH to EVMOS
 - ETH to TRON
 
 ### 目前支持生成地址的链
 - STEEM
 - ETH
 - TRON
 - EVMOS
 - COSMOS
 - TERRA
 - 大部分cosmos系的链

#### 使用示例

````
import steem_to_hdwallet as sd

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
pri_key="5JaRW6KRjMqj5bxCQAn37zZg76bDfoteSwZvP64j1ApSZaFtmKs"
eth_key=sd.get_eth_privkey(pri_key)
print(eth_key)

#从eth私钥获得对应steem私钥
privkey="6437ac6e07f7411e757fbc0113656c001e302ebca194fd944d45375f1ae639ae"
steem_key=sd.get_steem_privkey(privkey)
print(steem_key)

#从ETH地址得到evmos地址
raw_address="0xdd96de0d29092cbbf11d4739ec0d440752bdd307"
evmos_addr=sd.eth_to_bech32(raw_address, prefix="evmos")
print(evmos_addr)

#从ETH地址获得对应tron地址
raw_address="0xdd96de0d29092cbbf11d4739ec0d440752bdd307"
tron_addr = sd.eth_to_tron(raw_address)
print(tron_addr)

#获得某个用户公钥对应的eth地址
eth_addr_accounts=sd.get_eth_addr_accounts("justyy")
print(eth_addr_accounts)
````


#### 生成多链地址使用示例
````
from pyhd import hd_wallet_CreateFromMnemonic,hd_wallet_CreateFromprivatekey


ETH_DERIVATION_PATH = "m/44'/60'/0'/0"
COSMOS_DERIVATION_PATH = "m/44'/118'/0'/0"
TRON_DERIVATION_PATH = "m/44'/195'/0'/0"

mnemonics = "horn bonus still lobster exclude submit minimum above soap pilot antenna humble memory crew tooth exotic rich seek nominee cupboard sunny shine pause custom"

#ETH
addr_num=0
coins="ETH"
print(coins)
PATH=ETH_DERIVATION_PATH
wallet=hd_wallet_CreateFromMnemonic(mnemonics,PATH,addr_num,coins)
print(wallet,"\n")
private_key = "2c34e1161d70404fd5d8ae29d1c15cfb36b6e1d4c0134b25c8edd6f7a87c35d6"
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
addr_num=0
coins="STEEM"
print(coins)
PATH=ETH_DERIVATION_PATH
wallet=hd_wallet_CreateFromMnemonic(mnemonics,PATH,addr_num,coins)
print(wallet,"\n")
private_key = "2c34e1161d70404fd5d8ae29d1c15cfb36b6e1d4c0134b25c8edd6f7a87c35d6"
wallet=hd_wallet_CreateFromprivatekey(private_key,coins)
print(wallet)
print("----------------------------------------------------\n")

#COSMOS系，hdpath = "m/44'/118'/0'/0"的链
#例AKASH,格式：COSMOS_AKASH
coins="COSMOS_AKASH"
print(coins)
PATH=COSMOS_DERIVATION_PATH
wallet=hd_wallet_CreateFromMnemonic(mnemonics,PATH,addr_num,coins)
print(wallet,"\n")
private_key = "1f9d07b9ca4f99a0949302c428cefe67c90fc16ab53c3776e5f660a2dbb2e8f3"
wallet=hd_wallet_CreateFromprivatekey(private_key,coins)
print(wallet)
print("----------------------------------------------------\n")
````

#TERRA
coins="COSMOS_TERRA"
print(coins)
PATH="m/44'/330'/0'/0"
wallet=hd_wallet_CreateFromMnemonic(mnemonics,PATH,addr_num,coins)
print(wallet,"\n")
private_key = "1f9d07b9ca4f99a0949302c428cefe67c90fc16ab53c3776e5f660a2dbb2e8f3"
wallet=hd_wallet_CreateFromprivatekey(private_key,coins)
print(wallet)
print("----------------------------------------------------\n")
````

