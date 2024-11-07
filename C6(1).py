# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 11:57:30 2024

@author: Huỳnh Như Ngọc
"""

#Viết chương trình nhập vào 2 số nguyên a, b. Tính tổng, hiệu, tích,
 #thương, chia lấy dư, chia lấy nguyên của 2 số trên và in kết quả ra màn
 #hình. Kết quả phép chia làm tròn 2, 3 chữ số sau dấu chấm (ví dụ kết
 #quả 3.333333 thì làm tròn 3.333).
 
def tinh_toan():
    tong=a+b
    hieu=a-b
    tich=a*b
    thuong=round(a/b,3)
    chia_du=a%b
    chia_nguyen=a//b
    return tong,hieu,tich,thuong,chia_du,chia_nguyen
a=int(input("nhap a:"))
b=int(input("nhap b:"))
tong,hieu,tich,thuong,chia_du,chia_nguyen=tinh_toan()
print(f'tong:{tong}')
print(f'hieu:{hieu}')
print(f'tich:{tich}')
print(f'thuong:{thuong}')
print(f'chia lay du:{chia_du}')
print(f'chia lay nguyen:{chia_nguyen}')

# Viết chương trình cho phép nhập vào số nguyên dương N có 2 chữ số.
 #Xuất ra màn hình tổng các chữ số của N. Ví dụ: Nhập N=48, kết quả
 #xuất ra màn hình là 4 + 8 = 12

def nguyen_duong_N(N):
    hang_chuc=N//10
    hang_don_vi=N%10
    tong_chu_so=hang_chuc+hang_don_vi
    return tong_chu_so
N=int(input("nhap N:"))
tong=nguyen_duong_N(N)

#Viết chương trình cho phép nhập vào giờ, phút và giây (ví dụ 8 39 50).
 #Hãy đổi ra giây và in kết quả ra màn hình

def tinh_giay():
    tong_giay=gio*3600+phut*60+giay+60
    return tong_giay
gio=int(input("nhap gio:"))
phut=int(input("nhap phut:"))
giay=int(input("nhap giay:"))
tong=tinh_giay()

#Viết chương trình nhập vào năm sinh, in ra tuổi. Ví dụ nhập 1988 in ra
 #(giả sử năm hiện tại là 2023): Ban sinh nam 1988 vay ban 35 tuoi

def tinh_tuoi():
    tuoi=nam_hien_tai-nam_sinh
   
    return tuoi
nam_sinh=int(input("nhap nam sinh cua ban:"))
nam_hien_tai=2024
    


if __name__=="__main__":
    tinh_toan()
    print(f'tong {N} la:',nguyen_duong_N(N))
    print(f'tong giay là:',tinh_giay())
    print(f'ban sinh nam {nam_sinh} z ban',tinh_tuoi())