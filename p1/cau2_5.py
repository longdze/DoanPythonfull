import random
import os
import pickle

def main():
    m = int(input('nhap m= '))
    x = [random.random() for i in range(m)]
    print(x)
    taptin=input('ten tap tin:')
    f=open(taptin,"w")
    f.write(str(x) + '\n')
    print('da luu list x vao tap tin van ban')
    y = sorted(x)
    print('sap xep list theo chieu giam dan:', y)
    f.write(str(y) + '\n')
    print('da luu list y vao tap tin van ban')
    vitri = []
    n=float(input('nhap so can tim kiem n= '))
    for i in range(len(x)):
        if x[i]==n:
            vitri.append(i)
    if len(vitri)==0:
        print('khong tim thay so',n)
    else:
        print('vi tri n la',vitri)
    return x

if __name__=="__main__":
    main()
