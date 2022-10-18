import os
import codecs
import elg_decy as eleDecy
def decryption(C,d,n):
    P = []
    for i in C:
        P.append(chr((i**d)%n))
    return P

def main():
    FileName = 'Message.txt'
    fd = codecs.open(FileName,'r','utf-8')
    SampleData = fd.read()
    fd.close()
    print("Sample data is ",*SampleData)
    
    lst=eleDecy.main()
    n=int(lst[0])
    
    C = []
    for i in SampleData:
        C.append(ord(i))
    print(C)

    d = int(input("Enter Private Key : "))
    
    P = decryption(C,d,n)
    print(P)

    os.remove("elgamal_keys.txt")
    os.remove("Message.txt")

if __name__ == '__main__':
    main()