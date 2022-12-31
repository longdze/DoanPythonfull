from p3.nhanvien import *
class NhanVien:
    listNhanVien = []
    def __init__(self,fullname: str,age:int,salary:int):
        self.hoten =fullname
        self.tuoi = age
        self.luong = salary

    def nhap_NhanVien():
        n = int(input('nhap so nhan vien can them: '))
        for i in range(n):
            fullname = input("Nhap ten nhan vien: ")
            age = int(input("Nhap tuoi nhan vien: "))
            salary = int(input('Nhap luong nhan vien:'))
            nv = fullname, age, salary
            print(nv)
            self.listNhanVien.append(nv)
        print()

    # def hien_thi(self, listNhanVien=None):
    #     print(listNhanVien)
    #     return listNhanVien
    # def sap_xep_do_tuoi_giam(self,listNhanVien=None):
    #     z=sorted(listNhanVien,age,reverse=True)
    #
    # def luu_list(self):
    #     taptin = input('ten tap tin:')
    #     file = f.open(taptin, 'wb')
    #     pickle.dump(x, file)
    #
    # def doc_dt_tu_tap_nhi_phan(self):
    #     p=input('nhap tap tin nhi phan:')
    #     with open(p,'rb') as f:
    #         b=f.read()
    #         print(b)
    #

