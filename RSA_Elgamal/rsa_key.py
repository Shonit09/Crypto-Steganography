import math
import random as rm
import elg_key as eleKey
import elg_ency as elgEncy

def isEven(num):
    if num & 1 == 0:
        return True
    return False

def isPrime(num):
    if isEven(num):
        return False
    for i in range(2 , int(math.sqrt(num))+1):
        if num % i == 0:
            return False
        else:
            return True
    
def GCD(small , big):
    for i in range(small , 0 , -1):
        if big % i == 0 and small % i == 0:
            return i
        else:
            return 1

def nmGenerator(p,q):
    return p*q , (p-1)*(q-1)

def eGenerator(m):
    eArr = []
    for i in range(1,10):
        if GCD(i,m)==1:
            eArr.append(i)
    while True: 
        e = rm.choice(eArr)
        if e > 1 and e < m:
            return e

def dGenerator(e,m):
    k=1
    while(True):
        d=((k*m)+1)/e
        if(int(d)-d==0):
            return int(d)
        else:
            k+=1

def main():
    
    eleKey.main()
    p=0
    q=0
    PrimeList = [x for x in range(10,100) if isPrime(x)]
    while True:
        p = rm.choice(PrimeList)
        q = rm.choice(PrimeList)
        if p != q:
            break
    if(isPrime(p) and isPrime(q)):
        n,m = nmGenerator(p,q)
        e = eGenerator(m)
        print("n = ",n,"e = ",e)
        fd = open("rsa_key.txt","w")
        fd.write(str(n)+'\n'+str(e))
        fd.close()
        elgEncy.main()

        d = dGenerator(e,m)
        print("private key is : ",d)

if __name__ == '__main__':
    main()
