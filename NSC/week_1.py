def encrypt(arr,key):
    for i in range(len(arr)):
        n=(ord(arr[i])+key)
        if ord(arr[i])<91 and n>=91:
            n=65+(n-91)
        elif ord(arr[i])<=122 and n>122:
            n=97+(n-123)
            
        arr[i]=chr(n)
    return arr

def decrypt(arr,key):
    for i in range(len(arr)):
        n=(ord(arr[i])-key)
        if (ord(arr[i])>=65 and n<65) or (ord(arr[i])>=97 and n<97):
            n=(n+26)
        arr[i]=chr(n)
    return arr

s=input('enter input text: ')
#print(s)
arr=[]
for i in s:
    arr.append(i)
   
key=int(input('enter key: '))
ct=encrypt(arr,key)
print('Cypher text: ',''.join(ct))
print('decrypted text: ',''.join(decrypt(ct,key)))


'''

AbcxyzXYZ
3

DefabcABC

AbcxyzXYZ
'''