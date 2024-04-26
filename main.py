import os
import json
import hashlib
from bitcoinlib.transactions import Transaction, Input, Output

def validate_transaction(transaction_data):
    try:
        return True  
    except Exception as e:
        print(f"Transaction validation failed: {e}")
        return False

def mine_block(valid_transactions):
    version = 2
    prev_block = "0000000000000000000000000000000000000000000000000000000000000000"
    merkle_root = calculate_merkle_root(valid_transactions)
    time = 1633760708  
    bits = "ffff000000000000000000000000000000000000000000000000000000000000"
    nonce = 0

    coinbase_tx = create_coinbase_transaction()
    coinbase_tx_serialized = coinbase_tx.serialize()

    block_header = f"{version},{prev_block},{merkle_root},{time},{bits},{nonce}"

    block_txids = [coinbase_tx.txid] + [tx.txid for tx in valid_transactions]

    return block_header, coinbase_tx_serialized, block_txids

def calculate_merkle_root(transactions):
    return "1234567890abcdef"

def create_coinbase_transaction():
    # Create a simple coinbase transaction
    coinbase_tx = Transaction()
    coinbase_tx.add_input(Input())  
    coinbase_tx.add_output(Output())
    return coinbase_tx

def main():
    mempool_dir = 'mempool'
    valid_transactions = []

    # Iterate over each file in the directory
    for filename in os.listdir(mempool_dir):
        if filename.endswith('.json'):
            file_path = os.path.join(mempool_dir, filename)

            # Read the transaction data from the file
            with open(file_path, 'r') as file:
                transaction_data = file.read()

            # Validate the transaction
            if validate_transaction(transaction_data):
                # If valid, add to list of valid transactions
                valid_transactions.append(Transaction.from_json(transaction_data))

    # Mine valid transactions into a block
    block_header, coinbase_tx_serialized, block_txids = mine_block(valid_transactions)

    # Write output to output.txt
    with open('output.txt', 'w') as output_file:
        output_file.write(f"{block_header}\n")
        output_file.write(f"{coinbase_tx_serialized}\n")
        for txid in block_txids:
            output_file.write(f"{txid}\n")

if __name__ == '__main__':
    main()
