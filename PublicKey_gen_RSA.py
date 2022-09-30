import math
import random as rm
from tkinter import E

def isEven(num):#function to find if number is even or odd
    if num&1==0:
        return True
    return False

def isPrime(num):#function to fine if number is prime
    if(isEven(num)):
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if(num%i==0):
            return False
        else:
            return True

def GCD(small,big):
    for i in range(small,0,-1):
        if big%i==0 and small%i==0:
            return i;
        else:
            return 1

def nmGenerator(p,q):
    return p*q,(p-1)*(q-1)

def pk1(m):#public key generator
    eArr=[]
    for i in range(1,10):
        if GCD(i,m)==1:
            eArr.append(i)
    while True:
        e=rm.choice(eArr)
        if e>1 and e<m:
            return e

def pk2(e,m):#private key generator
    e1=e%m
    for i in range(m):
        if(e1*i)%m==1:
            return i

def main():
    PrimeList=[x for x in range(10,200) if isPrime(x)]

    while True:
        p=rm.choice(PrimeList)
        q=rm.choice(PrimeList)
        if p!=q:
            break

    if isPrime(p) and isPrime(q):
        n,m=nmGenerator(p,q)
        e=pk1(m)
        fd=open("Repository.txt","w")
        fd.write(str(n)+"\n"+str(e))
        fd.close()
        d=pk2(e,m)
        print("private key is: ",d)

if __name__=='__main__':
    main()
