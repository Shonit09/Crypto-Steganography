import RsaPublicKeyDist as RSA1
import RsaSender as RSA2
import RsaReceiver as RSA3
import PIL.Image as pimg
import Histo as h
import mulitprocessing as mp

def getRGBfromI(RGBint):#generate RGB from int
    blue=RGBint&255
    green=(RGBint>>8)&255
    red=(RGBint>>16)&255
    return red,green,blue

def getIfromRGB(rgb):#generate int from RGB
    red=rgb[0]
    green=rgb[1]
    blue=rgb[2]
    RGBint=(red<<16)+(green<<8)+blue
    return RGBint

def main():
    RSA1.main()
    FileNam='Repository.txt'
    fd=open(FileName)
    n=int(fd.readline())
    e=int(fd.readline())
    fd.close()
    length=0
    while length!=16:
        P=input("Enter the username size of 8 characters:")
        P+=input("Enter the password size of 8 characters:")
        length=len(P)

    data1=RSA2.encryption(P,e,n)
    print("Encrypted data is: ",data1)

    ImageToOpen=str(input("Enter Image to process: "))
    Image=pimg.open(ImageToOpen)
    ImageToProcess=Image.load()

    for j in range(16):
        r,g,b=getRGBforI(data1[j])
        #print rgb value for each entry in cipher text
        ImageToProcess[0,j]=(r,g,b)
        #hide data
        Image.save("s2.png")

        print("for Decryption")
        ImagetoOpen1=str(input("Enter Image to process:"))
        Image1=pimg.open(ImagetoOpen1)
        ImagetoProcess1=Image1.load()

        data1=[]
        for j in range(16):
            a=getIfromRGB(ImageToProcess1[0,j])
            #getting value of cipher text from image
            data1.append(a)

            FileName='Repository.txt'
            fd=open(FileName)
            n=int(fd.readline())
            fd.close()

            C=data1
            d=int(input("Enter Private Key: "))
            P=RSA3.decryption(C,d,n)
            print("username is :",str(P).replace(',',"").replace("'","").replace("","")[1:-9])
            print("username is :",str(P).replace(',',"").replace("'","").replace("","")[9:-1])
            print("histogram comparison")
            p1=mp.Process(target=h.draw,args=("s1.jpg"))
            p1=mp.Process(target=h.draw,args=("s2.jpg"))
            p1.start()
            p2.start()

if __name__=='__main__':
    main()