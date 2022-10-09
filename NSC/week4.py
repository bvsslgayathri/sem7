import random
p=int(input("enter p value: "))
q=int(input("enter q value: "))
n=p*q

fi_n=(p-1)*(q-1)

e=fi_n-1

def gcd(n1,n2):
    c=0
    for i in range(1,min(n1,n2)+1):
        if n1%i==0 and n2%i==0:
            c+=1
    if c==1:
        return 1
    else:
        return 0

while e>0:
    if gcd(e,fi_n)==1:
        break
print("the value of e obtained is ",e)

# e=3
m=int(input("enter message: "))
def encrypt(m,e):
    global n
    return pow(m,e) % n
def decrypt(ct,d):
    global n
    return pow(ct,d) % n

ct=encrypt(m,e)
print("Cypher text is ",ct)

# d=(1+(2*fi_n))//e
d=2
while (e*d) % fi_n !=1:
    d+=1

decrypted_text=decrypt(ct,d)
print("decrypted text is ",decrypted_text)


'''
p-3
q-7
e-11
mess-12
ct-3
dt-12

'''