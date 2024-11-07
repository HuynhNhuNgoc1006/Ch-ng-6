# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 10:18:06 2024

@author: Huỳnh Như Ngọc
"""

#Viết chương trình nhập vào 4 số nguyên a, b, c, d. Tính trung bình cộng
#của 4 số trên và in kết quả ra màn hình

def tbc():
    return (a+b+c+d)/4
a=int(input("nhap a:"))
b=int(input("nhap b:"))
c=int(input("nhap c:"))
d=int(input("nhap d:"))
tbcong=tbc()
print(f"tbc la:{tbcong}")

#Viết chương trình nhập vào 2 số nguyên a, b. Tính tổng, hiệu, tích,
#thương, chia lấy dư, chia lấy nguyên của 2 số trên và in kết quả ra màn
#hình. Kết quả phép chia làm tròn 2, 3 chữ số sau dấu chấm (ví dụ kết
#quả 3.333333 thì làm tròn 3.333)

def tinh_toan(a,b):
    tong=a+b
    hieu=a-b
    tich=a*b
    thuong=round(a/b,3)
    chia_du=a%b
    chia_nguyen=a//b
    return tong, hieu, tich, thuong, chia_du, chia_nguyen
a=int(input("nhap a:"))
b=int(input("nhap b:"))
tong,hieu,tich,thuong,chia_du,chia_nguyen=tinh_toan(a,b)
print(f"Tong:{tong}")
print(f'Hieu:{hieu}')
print(f'Tich:{tich}')
print(f'Thuong:{thuong}')
print(f'Chia lay du:{chia_du}')
print(f'Chia lay nguyen:{chia_nguyen}')


#Viết chương trình cho phép nhập vào số nguyên dương N có 2 chữ số.
#Xuất ra màn hình tổng các chữ số của N. Ví dụ: Nhập N=48, kết quả
#xuất ra màn hình là 4 + 8 = 12

def tinh_tong_chu_so(N):
    hang_chuc=N//10
    hang_dvi=N%10
    tong_chu_so=hang_chuc+hang_dvi
    return  tong_chu_so

N=int(input("nhap N:"))
if 10<=N<=99:
    tong=tinh_tong_chu_so(N)
    print(f'Tong {N} la:{tong}')
else:
        print("sai roi nhap lai")
        
        
#Viết chương trình cho phép nhập vào giờ, phút và giây (ví dụ 8 39 50).
#Hãy đổi ra giây và in kết quả ra màn hình.
 

def chuyen_ve_giay():
    tong_giay=gio*3600+phut*60+60+giay
    return tong_giay
gio=int(input("nhap gio:"))
phut=int(input("nhap phut:"))
giay=int(input("nhap giay:"))
tong_giay=chuyen_ve_giay()
print(f'tong giay la:{tong_giay}')

#Viết chương trình nhập vào năm sinh, in ra tuổi. Ví dụ nhập 1988 in ra
#(giả sử năm hiện tại là 2023): Ban sinh nam 1988 vay ban 35 tuoi
    

def tinh_tuoi():
    tuoi=nam_hien_tai-nam_sinh
    return tuoi
nam_sinh=int(input("nhap nam sinh:"))
nam_hien_tai=2024
tuoi=tinh_tuoi()
print(f'z bn {tuoi} tuoi.')

# Nhập vào 3 số a, b, c. Sau đó in ra phương trình bậc 2 dạng
 #aX^2 + bX + C = 0
 #Ví dụ nhập a = 2, b = 5, c = 4 thì in ra 2X^2 + 5X + 4 = 0

def pt_bac2(a,b,c):
    pt=f"phuong trinh bac 2: {a}x^2+{b}x+{c}=0"
    return pt
a=int(input("nhap a:"))
b=int(input("nhap b:"))
c=int(input("nhap c:"))
pt=pt_bac2(a,b,c)
print(pt)

#Menu




    
if __name__=="__mian__":
    tbc()
    tinh_toan(a,b)
    tinh_tong_chu_so(N)
    chuyen_ve_giay()
    tinh_tuoi()
    pt_bac2(a,b,c)
    
    