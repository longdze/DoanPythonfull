from nhanvien import NhanVien
import os
import pickle

def luu_tap_tin_nhi_phan(thumuc:str, ten_tap_tin: str, obj: NhanVien):
    try:
        with open(os.path.join(thumuc, ten_tap_tin),'wb') as f:
            pickle.dump(obj, f)
        print('Hoàn thành quá trình ghi dữ liệu')
    except Exception as e:
        print('Xảy ra lỗi trong quá trình ghi dữ liệu')
