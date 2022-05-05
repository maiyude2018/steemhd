from pyhd import hd_wallet_CreateFromMnemonic,hd_wallet_CreateFromprivatekey


ETH_DERIVATION_PATH = "m/44'/60'/0'/0"
COSMOS_DERIVATION_PATH = "m/44'/118'/0'/0"
TRON_DERIVATION_PATH = "m/44'/195'/0'/0"

mnemonics = "horn bonus still lobster exclude submit minimum above soap pilot antenna humble memory crew tooth exotic rich seek nominee cupboard sunny shine pause custom"

#ETH
addr_num=0
coins="ETH"
PATH=ETH_DERIVATION_PATH
wallet=hd_wallet_CreateFromMnemonic(mnemonics,PATH,addr_num,coins)
print(wallet)
private_key = "2c34e1161d70404fd5d8ae29d1c15cfb36b6e1d4c0134b25c8edd6f7a87c35d6"
wallet=hd_wallet_CreateFromprivatekey(private_key,coins)
print(wallet)

#TRON
coins="TRON"
PATH=TRON_DERIVATION_PATH
wallet=hd_wallet_CreateFromMnemonic(mnemonics,PATH,addr_num,coins)
print(wallet)
private_key = "29efb52958f443e522fe52b89856c601c41b8910a0ef1d7f8b9beb2f11a8e684"
wallet=hd_wallet_CreateFromprivatekey(private_key,coins)
print(wallet)

#COSMOS
coins="COSMOS"
PATH=COSMOS_DERIVATION_PATH
wallet=hd_wallet_CreateFromMnemonic(mnemonics,PATH,addr_num,coins)
print(wallet)
private_key = "1f9d07b9ca4f99a0949302c428cefe67c90fc16ab53c3776e5f660a2dbb2e8f3"
wallet=hd_wallet_CreateFromprivatekey(private_key,coins)
print(wallet)

#EVMOS
addr_num=0
coins="EVMOS"
PATH=ETH_DERIVATION_PATH
wallet=hd_wallet_CreateFromMnemonic(mnemonics,PATH,addr_num,coins)
print(wallet)
private_key = "2c34e1161d70404fd5d8ae29d1c15cfb36b6e1d4c0134b25c8edd6f7a87c35d6"
wallet=hd_wallet_CreateFromprivatekey(private_key,coins)
print(wallet)

addr_num=0
coins="STEEM"
PATH=ETH_DERIVATION_PATH
wallet=hd_wallet_CreateFromMnemonic(mnemonics,PATH,addr_num,coins)
print(wallet)
private_key = "2c34e1161d70404fd5d8ae29d1c15cfb36b6e1d4c0134b25c8edd6f7a87c35d6"
wallet=hd_wallet_CreateFromprivatekey(private_key,coins)
print(wallet)

