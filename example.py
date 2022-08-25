import steemhd.steem_to_hdwallet as sd


#Steem Public key & Steem Private key
account="maiyude"
passwd="helloworld"
keys=sd.get_key_steem(account,passwd)
print(keys)

#From Steem Public key get Steem Private key
key="5JaRW6KRjMqj5bxCQAn37zZg76bDfoteSwZvP64j1ApSZaFtmKs"
stm=sd.get_pubkey(key)
print(stm)

#Steem Public key  ==> ETH address
stm="STM7UpXLm8WGaBWZmcnCYD88zesBoXhGR6eV5HP6tKxtpmRhPfSit"
eth_addr=sd.get_eth_addr_fromsteem(stm)
print(eth_addr)

#Steem Public key  ==> TRON address
stm="STM7UpXLm8WGaBWZmcnCYD88zesBoXhGR6eV5HP6tKxtpmRhPfSit"
tron_addr=sd.get_tron_addr_fromsteem(stm)
print(tron_addr)

#Steem Public key  ==> COSMOS address
stm="STM7UpXLm8WGaBWZmcnCYD88zesBoXhGR6eV5HP6tKxtpmRhPfSit"
cosmos_addr=sd.get_cosmos_addr_fromsteem(stm)
print(cosmos_addr)

#STEEM Private key ==> ETH Private key
pri_key="5KLWLNT3v1s4tLKFYjrFb1hVpHFZkcA6syrNhapFU35DPd1ML6m"
eth_key=sd.get_eth_privkey(pri_key)
print("eth_key",eth_key)

#STEEM Private key ==> BTC Private key
pri_key="5KLWLNT3v1s4tLKFYjrFb1hVpHFZkcA6syrNhapFU35DPd1ML6m"
btc_key=sd.get_btc_privkey(pri_key)
print("btc_key1",btc_key)

#ETH Private key ==> STEEM Private key
privkey="c85064d7c3cba0fd71ea98e438899b579227a87bd1d9316503ef2dd2689294f7"
steem_key=sd.get_steem_privkey(privkey)
print("steem_key",steem_key)

#Private key ==> WIF Private key(BTC)
privkey="c85064d7c3cba0fd71ea98e438899b579227a87bd1d9316503ef2dd2689294f7"
btc_key=sd.privkey_towif(0x80,privkey,"01")
print("btc_key2",btc_key)

#Private key ==> WIF Private key(DOGE)
privkey="2542b1a3e16398a3860543e6343601518b97f2e94ed4fa1fdbe27d9096599077"
doge_key=sd.privkey_towif(0x9e,privkey,"01")
print("DOGE",doge_key)

#WIF Private key ==> RAW Private key
wif="L3w6UVfyrzoz9aFZD68PP85kBgjHZUBAx1vvn8FYrL9bgVRCyjhf"
btc_raw_key=sd.get_eth_privkey(wif)[:-2]
print("btc_raw_key",btc_raw_key)

#ETH address ==> COSMOS address
raw_address="0xdd96de0d29092cbbf11d4739ec0d440752bdd307"
evmos_addr=sd.eth_to_bech32(raw_address, prefix="evmos")
print(evmos_addr)

#ETH address ==> TRON address
raw_address="0xdd96de0d29092cbbf11d4739ec0d440752bdd307"
tron_addr = sd.eth_to_tron(raw_address)
print(tron_addr)

#TRON address ==> ETH address
raw_address="TWAs4uMQ1bVxksLdoCwkvgCZbqwLM6ScR2"
eth_addr = sd.tron_to_eth(raw_address)
print(eth_addr)

#Get someone account Steem Public key  ==> ETH address
eth_addr_accounts=sd.get_eth_addr_accounts("maiyude")
print(eth_addr_accounts)
