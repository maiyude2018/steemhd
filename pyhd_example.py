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

#Other COSMOS chains，hdpath = "m/44'/118'/0'/0"
#Example AKASH：COSMOS_AKASH
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
