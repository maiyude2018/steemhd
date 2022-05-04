### 这是一个可以计算steem公私钥的工具，支持把steem的公钥按照hdwallet的规则转换为其他链的地址

### 使用示例

````
import steem_to_hdwallet as sd

#从密码计算所有公私钥对
account="maiyude"
passwd="helloworld"
keys=sd.get_key_steem(account,passwd)
print(keys)
#=》{'account': 'maiyude', 'passwd': 'helloworld', 'owner_key': {'private': '5JuP8Zf4MS3QLhXn45cFYwxGe3xALyWTwD5VYE7AXAw3VKnaApq', 'public': 'STM7C1KJrC9wJ67EWzguECHy7Z9kYLJ5WJVzSgPf2sPHYiiMLFLHT'}, 'posting_key': {'private': '5J2b3Mjhw85yZZiB7M9oy2sLqZ6URfCmThV5N4pfuzJRduzoBPe', 'public': 'STM6Lhhdi8u5nrAJSDFpE4JpkB6EkuYaoas1j5gizCr178GbqSJGW'}, 'active_key': {'private': '5JaRW6KRjMqj5bxCQAn37zZg76bDfoteSwZvP64j1ApSZaFtmKs', 'public': 'STM7UpXLm8WGaBWZmcnCYD88zesBoXhGR6eV5HP6tKxtpmRhPfSit'}, 'memo_key': {'private': '5J7xaRhfA8Qf4ZK6NppoWXCsEPSXfABrchJa97iiqGrkcDEeJpF', 'public': 'STM7mGXBwmrYch3HmcBKJNac65evbmS5USDf3gqif4MZCtdM3aJZr'}}

#从steem私钥获得公钥
key="5JaRW6KRjMqj5bxCQAn37zZg76bDfoteSwZvP64j1ApSZaFtmKs"
stm=sd.get_pubkey(key)
print(stm)
#=》STM7UpXLm8WGaBWZmcnCYD88zesBoXhGR6eV5HP6tKxtpmRhPfSit

#从steem公钥获得对应eth地址
stm="STM7UpXLm8WGaBWZmcnCYD88zesBoXhGR6eV5HP6tKxtpmRhPfSit"
eth_addr=sd.get_eth_addr_fromsteem(stm)
print(eth_addr)
#=》0xdd96de0d29092cbbf11d4739ec0d440752bdd307

#从steem私钥获得对应eth私钥
pri_key="5JaRW6KRjMqj5bxCQAn37zZg76bDfoteSwZvP64j1ApSZaFtmKs"
eth_key=sd.get_eth_privkey(pri_key)
print(eth_key)
#=》6437ac6e07f7411e757fbc0113656c001e302ebca194fd944d45375f1ae639ae

#获得某个用户公钥对应的eth地址
eth_addr_accounts=sd.get_eth_addr_accounts("justyy")
print(eth_addr_accounts)
#=》{'account': 'justyy', 'owner': '0x634befaed597ccafb1899ac013c28e0dd8aeef6c', 'posting': '0x087eb3e28c2fdb8bde6184612f5ae6f38ba7005b', 'active': '0xab2b0b1305c279dd2c6af16fc3e9d22e5d98d3d2'}

#从steem公钥获得对应tron地址
stm="STM7UpXLm8WGaBWZmcnCYD88zesBoXhGR6eV5HP6tKxtpmRhPfSit"
tron_addr=sd.get_tron_addr_fromsteem(stm)
print(tron_addr)

#从steem公钥获得对应tron地址
stm="STM7UpXLm8WGaBWZmcnCYD88zesBoXhGR6eV5HP6tKxtpmRhPfSit"
tron_addr=sd.get_tron_addr_fromsteem(stm)
print(tron_addr)

````
