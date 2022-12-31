from p3.cau3_2 import *
from p3.cau3_3 import *
from p3.cau3_4 import *
from p3.cau3_5 import *
from p3.cau3_6 import *

def main():
    path = 'C:/Users/ACER/Documents/DoAn'
    ten_file = 'doan.txt'
    listnv=[]
    nhap_NhanVien(listnv)
    hien_thi_ra_man_hinh(listnv)
    sap_xep_doi_tuong(listnv)
    luu_tap_tin_nhi_phan(path,ten_file, listnv)
    doc_tap_tin(path, ten_file)

if __name__=='__main__':
    main()
