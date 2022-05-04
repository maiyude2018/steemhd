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

#从steem私钥获得对应eth私钥
pri_key="5JaRW6KRjMqj5bxCQAn37zZg76bDfoteSwZvP64j1ApSZaFtmKs"
eth_key=sd.get_eth_privkey(pri_key)
print(eth_key)

#获得某个用户公钥对应的eth地址
eth_addr_accounts=sd.get_eth_addr_accounts("justyy")
print(eth_addr_accounts)
