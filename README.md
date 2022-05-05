### 这是一个可以计算steem公私钥的工具，支持把steem的公钥按照hdwallet的规则转换为其他链的地址

#### 目前支持
 - STEEM to ETH
 - STEEM to TRON
 - STEEM to COSMOS
 - ETH to EVMOS
 - ETH to TRON

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
