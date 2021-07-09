from os import read
import time
import hashlib

readfile = open("C:\\Users\\cho03\\Desktop\\programming\\Codes\\miningLog.txt", 'r')
writefile = open("C:\\Users\\cho03\\Desktop\\programming\\Codes\\miningLog.txt", 'w')

MAX_NONCE = int(1e10)
DIFFICULTY = 5

previous_hash = '00000000000000000006dfdf4ae77bc817ae825858884e68c016fbf36298e793'

new_hash = None

start_time = time.time()

def makeBlock(block_number, transactions, previous_hash):
    for nonce in range(MAX_NONCE):
        text = str(block_number) + str(transactions) + str(previous_hash) + str(nonce)
        new_hash = hashlib.sha256(text.encode('ascii')).hexdigest()

        if new_hash.startswith('0' * DIFFICULTY):
            print(f'Hash: {new_hash}')
            print(f'Nonce: {nonce}')
            print(f'Transactions: {transactions}')
            print(f'Block_number: {block_number}')
            break
    print('\\n')
    previous_hash = new_hash
    block_number += 1
    return previous_hash, block_number

    if new_hash is None:
        print('Cannot find new hash')

writefile.write(makeBlock(12345,str("asdasd"),1234567))
lines = readfile.readline()
print(lines)



print(f'Mining took {time.time() - start_time}s!')
