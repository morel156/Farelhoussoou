from itertools import product
i=1
r=1
def factoriel(i,r,n):
    i=1
    r=1
    while i <= n:
        r=r*i
        i+=1
    return r
def multiple(i):
    for i in range(1,51):
        if i%3==0:
            print(i,"HOUSSOU")
        if i%5==0:
            print(i,"Farel")
        if i%3==0 and i%5==0:
            print(i,"HOUSSOU Farel")

n=int(input("entrer un nombre:"))
print("le factoriel est",factoriel(i,r,n))
print(multiple(i))

input()


























































































































