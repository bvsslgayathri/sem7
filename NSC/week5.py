P=int(input("enter value of P: "))
G=int(input("enter value of G: "))


a=int(input("enter value of a: "))
x=pow(G,a) % P

b=int(input("enter value of b: "))
y=pow(G,b) % P

def alice(y,a,P):
    return pow(y,a) % P

def bob(y,a,P):
    return pow(x,b) % P


print("The private key a for Alice : ",a)
print("The private key a for bob : ",b)

ka=alice(y,a,P)

kb=bob(x,b,P)
if ka==kb:
    print("Secret key for alice is ",ka)
    print("Secret key for bob is ",kb)


'''
P-23
G-9
a-4
b-3

ka-4
kb-3

sk-9

'''