from os import read
import time
import hashlib

readfile = open("C:\\Users\\cho03\\Desktop\\programming\\Codes\\miningLog.txt", 'r')
writefile = open("C:\\Users\\cho03\\Desktop\\programming\\Codes\\miningLog.txt", 'w')

f = open("C:\\Users\\cho03\\Desktop\\programming\\Codes\\miningLog.txt", 'r+')   
f.truncate(0)
    
max_nonce = int(1e10)

DIFFICULTY = 5

previous_hash = '000000000000000000064587uyhg4w7g98w59e98r8r9veweqer124889b9v658h'

new_hash = None

block_number = 0

transactions = "informations"

start_time = time.time()

def makeBlock(block_number, transactions, previous_hash):
    for nonce in range(max_nonce):
        text = str(block_number) + str(transactions) + str(previous_hash) + str(nonce)
        new_hash = hashlib.sha256(text.encode('ascii')).hexdigest()

        if new_hash.startswith('0' * DIFFICULTY):
            print(f'Hash: {new_hash}')
            print(f'Nonce: {nonce}')
            print(f'Transactions: {transactions}')
            print(f'Block_number: {block_number}')
            break
    print('\n')
    previous_hash = new_hash
    str_previous_hash = str(previous_hash)
    str_block_number = str(block_number)
    hashBack = str_previous_hash + str_block_number + transactions
    return hashBack

    if new_hash is None:
        print('Cannot find new hash')

while True:
    if block_number > 10:
        #10개의 블럭 생성시 강제 종료 
        break
    
    block = makeBlock(block_number, transactions, previous_hash)
    write_block = "Block"+ str(block_number) + "[" + block + "]"
    writefile.write(write_block)
    writefile.write('\n')
    print(block)
    print("\n")
    block_number += 1 
    
   
    






print(f'Mining took {time.time() - start_time}s!')
