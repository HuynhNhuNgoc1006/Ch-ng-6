# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 16:09:26 2024

@author: Huỳnh Như Ngọc
"""

def menu():
 print("=============MENU===========")
 print("1. Hu tieu")
 print("2. Chao long")
 print("3. Banh canh")
 print("4. Bun rieu")
 print("5. Pho bo")
 print("============================")
 luachon=int(input("Moi nhap lua chon: "))
 print("============================")
 if luachon ==1:
    print("1. Hu tieu")
 elif luachon ==2:
    print("2. Chao long")
 elif luachon ==3:
    print("3. Banh canh")
 elif luachon ==4:
    print("4. Bun rieu")
 elif luachon ==5:
    print("5. Pho bo")
 else:
    print(" Không hợp lệ")
    
#

import math
def phep_tinh():
    A=32**0.2-(1/64)**-0.25+(8/27)**(1/3)
    A_rounded=round(A,3)
 
    print("kp:",A_rounded)
    return A_rounded

import math
def can_bac():
    a=float(input("nhap a:"))
    b=float(input("nhap b:"))
    A1=((math.pow(a,1/2))-(math.pow(b,1/2)))/((math.pow(a,1/4))-(math.pow(b,1/4)))
    A2=((math.pow(a,1/2))+(math.pow(a*b,1/4)))/((math.pow(a,1/4))+(math.pow(b,1/4)))
    hieu=A1-A2
    print("ket qua:",hieu)
    return 
 
    
if __name__=="__main__":
    menu()
    phep_tinh()
    can_bac()