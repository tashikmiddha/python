from bitcoinlib.wallets import wallet 
w=wallet.create('AIOCkyrkwallet')
key1=w.getkey()
print(key1.address)