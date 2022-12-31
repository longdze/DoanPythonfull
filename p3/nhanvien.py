class NhanVien:
    listNhanVien = []
    def __init__(self,fullname: str,age:int,salary:int):
        self.hoten =fullname
        self.tuoi = age
        self.luong = salary

    def __str__(self)->str:
        message = '[ho ten: ' + self.hoten + '; tuoi: ' \
                  + str(self.tuoi) + '; luong: ' \
                  + str(self.luong) + ']'
        return message

    def __gt__(self, obj):
        return (self.tuoi > obj.tuoi)

    def __ge__(self, obj):
        return (self.tuoi >= obj.tuoi)

    def __lt__(self, obj):
        return (self.tuoi < obj.tuoi)

    def __le__(self, obj):
        return (self.tuoi <= obj.tuoi)

    def __eq__(self, obj):
        return (self.tuoi == obj.tuoi)


    # def nhap_NhanVien():
    #     n = int(input('nhap so nhan vien can them: '))
    #     for i in range(n):
    #         fullname = input("Nhap ten nhan vien: ")
    #         age = int(input("Nhap tuoi nhan vien: "))
    #         salary = int(input('Nhap luong nhan vien:'))
    #         nv = fullname, age, salary
    #         print(nv)
    #         self.listNhanVien.append(nv)
    #     print()
    # def sap_xep_nv_giam_dan():
    #     z=sorted(listNhanVien, x: x._age,reserve=False)
    #
    # def hien thi_NhanVien():



