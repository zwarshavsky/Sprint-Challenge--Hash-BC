import hashlib
import requests

import sys

from uuid import uuid4

from timeit import default_timer as timer

import random

import json


def proof_of_work(last_proof):
    """
    Multi-Ouroboros of Work Algorithm
    - Find a number p' such that the last five digits of hash(p) are equal
    to the first five digits of hash(p')
    - IE:  last_hash: ...AE912345, new hash 12345888...
    - p is the previous proof, and p' is the new proof
    - Use the same method to generate SHA-256 hashes as the examples in class
    """

    start = timer()

    print("Searching for next proof")

    
    # block_string = json.dumps(last_proof, sort_keys=True)
    # print("initiating proof with block string:",block_string)
    proof = 0
    while not valid_proof(last_proof, proof):
        proof += 1
    print("Proof found: " + str(proof) + " in " + str(timer() - start))
    return proof


def valid_proof(last_proof, proof):
    """
    Validates the Proof:  Multi-ouroborus:  Do the last five characters of
    the hash of the last proof match the first five characters of the hash
    of the new proof?

    IE:  last_hash: ...AE912345, new hash 12345E88...
    """
    # guess = f"{last_hash}{proof}".encode()
    guess1 = f"{proof}".encode()
    guess_hash1 = hashlib.sha256(guess1).hexdigest()
    guess2 = f"{last_proof}".encode()
    guess_hash2 = hashlib.sha256(guess2).hexdigest()
    if guess_hash2[-5:] == guess_hash1[:5]:
        print(guess_hash2,guess_hash1)
    # if last_hash[-5:] == guess_hash[:5]:
    #     print(last_hash,guess_hash)
    return guess_hash1[:5] == guess_hash2[-5:]


if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        # node = "https://lambda-coin.herokuapp.com/api"
        node = "https://lambda-coin-test-1.herokuapp.com/api"

    coins_mined = 0

    # Load or create ID
    f = open("my_id.txt", "r")
    id = f.read()
    print("ID is", id)
    f.close()

    if id == 'NONAME\n':
        print("ERROR: You must change your name in `my_id.txt`!")
        exit()
    # Run forever until interrupted
    while True:
        # Get the last proof from the server
        r1 = requests.get(url=node + "/last_proof")
        data1 = r1.json()
        # print("last_proof recieved:",data1)
        # r2 = requests.get(url=node + "/full_chain")
        # data2 = r2.json()
        # for block in data2["chain"]:
        #     if data1["proof"] == block["proof"]:
        #         previous_hash = block["previous_hash"]

        # new_proof = proof_of_work(previous_hash,data1.get('proof'))
        # new_proof = proof_of_work(previous_hash)
        new_proof = proof_of_work(data1.get('proof'))
        print("new_proof:",new_proof)

        post_data = {"proof": new_proof,
                     "id": id}

        r = requests.post(url=node + "/mine", json=post_data)
        data = r.json()
        if data.get('message') == 'New Block Forged':
            coins_mined += 1
            print("Total coins mined: " + str(coins_mined))
        else:
            print(data.get('message'))