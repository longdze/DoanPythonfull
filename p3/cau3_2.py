from nhanvien import NhanVien

def nhap_NhanVien(listnv:list):
    n = int(input('Nhap so nhan vien can them: '))
    for i in range(n):
        fullname = input("Nhap ten nhan vien: ")
        age = int(input("Nhap tuoi nhan vien: "))
        salary = int(input('Nhap luong nhan vien:'))
        nv = NhanVien(fullname, age, salary)
        listnv.append(nv)
        print(nv)





# def hien_thi(self, listNhanVien=None):
#     print(listNhanVien)
#     return listNhanVien
# # def sap_xep_do_tuoi_giam(self,listNhanVien=None):
# #     z=sorted(listNhanVien,age,reverse=True)
#
# def luu_list(self):
#     taptin = input('ten tap tin:')
#     file = f.open(taptin, 'wb')
#     pickle.dump(x, file)
#
# def doc_dt_tu_tap_nhi_phan(self):
#     path='C:/Users/ACER/Documents/doan.txt'
#     with open(path,'rb') as f:
#         b=f.read()
#         print(b)
