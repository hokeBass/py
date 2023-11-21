from web3 import Web3

avax_infura_url = 'https://avax.meowrpc.com' 
w3 = Web3(Web3.HTTPProvider(avax_infura_url))

my_address = '' #Wallet address
private_key = '' #private key

hex_data = '0x646174613a2c7b2270223a227072632d3230222c226f70223a226d696e74222c227469636b223a22706f6c73222c22616d74223a22313030303030303030227d'
current_gas_price = w3.eth.gas_price
nonce = w3.eth.get_transaction_count(my_address)
chain_id = 43114

number_of_transactions = 10

for i in range(number_of_transactions):
    transaction = {
        'to': my_address,
        'value': 0,
        'gas': 2000000,
        'gasPrice': current_gas_price,
        'nonce': nonce + i,
        'chainId': chain_id,
        'data': hex_data
    }

    signed_txn = w3.eth.account.sign_transaction(transaction, private_key)
    txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print(f'交易已发送，TX: {txn_hash.hex()}')
