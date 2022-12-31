import random
import pickle

def sinh_ngau_nhien():
    a = -10
    b = 10
    n = int(input('n='))
    x = [(b-a)*random.random() + a for i in range(n)]
    print(x)
    return x
x=sinh_ngau_nhien()

def sap_xep_list_tang(x):
    x1=sorted(x)
    print('Sap xep tang dan',x1)
    return x1
sap_xep_list_tang(x)

def sap_xep_list_giam(x):
    x2 = sorted(x,reverse=True)
    print('Sap xep giam dan',x2)
    return x2
sap_xep_list_giam(x)

def tim_kiem_so_n(x):
    try:
        vitri = []
        n=float(input('Nhap so can tim n= '))
        for i in range(len(x)):
            if x[i]==n:
                vitri.append(i)
        if len(vitri)==0:
            print('Khong tim thay so',n)
        else:
            print('Vi tri n la',vitri)
        return x
    except Exception as e:
        print(e)
tim_kiem_so_n(x)

def luu_list():
    taptin=input('Ten tap tin:')
    m = int(input("Nhap la so 1 la 'w': luu tap tin van ban hoac so 2 la 'wb': luu tap tin nhi phan: "))
    w=1
    wb=2
    if m == wb:
        file = open(taptin,'wb' )
        pickle.dump(x,file)
        print('Da luu tap tin nhi phan')
    else:
        if m == w:
            file = open(taptin,'w' )
            file.write(','.join(map(str,x)))
            print('Da luu tap van ban')
        else:
            print('khong chay')
luu_list()