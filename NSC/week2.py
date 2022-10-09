import numpy as np
from egcd import egcd
key=[[0 for j in range(3)] for i in range(3)]
cyp=[[0 for j in range(3)] for i in range(3)]
inp=[0 for i in range(3)]

def encrypt(k,s):
    l=0
    global key,inp
    for i in range(3):
        for j in range(3):
            key[i][j]=ord(k[l])%65
            l+=1
    
    for i in range(len(s)):
        inp[i]=ord(s[i])%65
    
    inp=np.array(inp)
    key=np.array(key)
    res=np.dot(key,inp)
    res1=[0 for i in range(3)]
    for i in range(len(res)):
        r=res[i]%26

        res1[i]=chr(r+65)

    enc_val=''.join(res1)
    return enc_val

def matrix_mod_inv(matrix, modulus):

    det = int(np.round(np.linalg.det(matrix)))  # Step 1)
    det_inv = egcd(det, modulus)[1] % modulus  # Step 2)
    matrix_modulus_inv = (
        det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    )  # Step 3)

    return matrix_modulus_inv

def decrypt(ct):
    global key,inp,cyp
    for i in range(len(ct)):
        cyp[i]=ord(ct[i])%65
    
    cyp=np.array(cyp)
    kinv=matrix_mod_inv(key,26)
    Kinv=np.array(kinv)
    res=np.dot(Kinv,cyp)
    plain=""
    for i in res:
        plain+=chr((i%26)+65)
    return plain

s=input()
k=input()

enc_val=encrypt(k,s)
print("cypher text: ",enc_val)

dec_val=decrypt(enc_val)
print("decryptd plain text: ",dec_val)


'''
ACT
GYBNQKURP

POH

ACT

'''