from os import read
import time
import hashlib

readfile = open("C:\\Users\\cho03\\Desktop\\programming\\Codes\\miningLog.txt", 'r')
writefile = open("C:\\Users\\cho03\\Desktop\\programming\\Codes\\miningLog.txt", 'w')

f = open("C:\\Users\\cho03\\Desktop\\programming\\Codes\\miningLog.txt", 'r+')   
f.truncate(0) #블록 저장 경로에 적힌 블록 초기화
    
max_nonce = int(1e10) #논스의 최댓값()

DIFFICULTY = 5 #난이도 설정 (해쉬 앞부분에 0이 몇개 나와야하는지를 난이도로 설정 )

previous_hash = '000000000000000000064587uyhg4w7g98w59e98r8r9veweqer124889b9v658h' #임의의 64자리 해쉬를 설정함

new_hash = None #새 해쉬가 올 변수 설정

block_number = 0 #블록의 번호 설정 0번블록은 초기값

transactions = "informations" #거래 내역 문자열

start_time = time.time() #소요 시간을 측정

def makeBlock(block_number, transactions, previous_hash): #블록 번호 , 거래내용 , 이전 해쉬를 넣으면 
    for nonce in range(max_nonce): # max_nonce까지 반복
        text = str(block_number) + str(transactions) + str(previous_hash) + str(nonce) #블록 번호 , 거래내역 , 전 블록의 해쉬 , 논스를 더해서 새로운 문자열 만듬
        new_hash = hashlib.sha256(text.encode('ascii')).hexdigest() #new_hash변수에 text를 sha-256방식으로 인코딩한 64자리 해쉬를 저장

        if new_hash.startswith('0' * DIFFICULTY): #해쉬가 난이도 * 0 으로 시작한다면
            print(f'Hash: {new_hash}')
            print(f'Nonce: {nonce}')
            print(f'Transactions: {transactions}')
            print(f'Block_number: {block_number}')
            break 
    print('\n')
    previous_hash = new_hash
    str_previous_hash = str(previous_hash)
    str_block_number = str(block_number)
    hashBack = str_previous_hash + str_block_number + transactions #저장되는 블록의 형식
    return hashBack

    if new_hash is None:
        print('Cannot find new hash')

while True:
    if block_number > 10:
        #10개의 블럭 생성시 강제 종료 
        break
    
    block = makeBlock(block_number, transactions, previous_hash)
    write_block = "Block"+ str(block_number) + "[" + block + "]" #기록할 블록 형식
    writefile.write(write_block) #개별 파일에 기록 저장
    writefile.write('\n')
    print(block)
    print("\n")
    block_number += 1 
    
print(f'Mining took {time.time() - start_time}s!')
