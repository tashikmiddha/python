from hashlib import sha256
MAX = 1000000000000000000
import time


def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()


def mine(block_number, transactions, previous_hash, prefix_zeroes):
    prefix_str = '0'*prefix_zeroes
    for nonce in range(MAX):
        text = str(block_number)+transactions+previous_hash+str(nonce)
        new_hash = SHA256(text)
        if (new_hash.startswith(prefix_str)):
            print(
                f"yay! successfully mined bitcoin with nonce value : {nonce}")
            return new_hash
    raise BaseException(f"couldn't find correct has after trying {MAX} times")


if __name__ == '__main__':
    transactions = '''
    tashik->hritik->600
    hritik->tashik->5000
    '''
    difficulty = 6
    start=time.time()
    print("start mining")
    new_hash = mine(5, transactions, '0000760440f033a33154639f1af83966f927942b18a266e61757618e2fe92ca8', difficulty)
    total_time=str((time.time()-start))
    print(f"end mining . mining took :{total_time} seconds")
    print(new_hash) 
