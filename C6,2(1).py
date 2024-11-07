# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 16:37:30 2024

@author: Huỳnh Như Ngọc
"""

#Menu

def menu():
    print("=======MENU======")
    print("1.hu tieu")
    print("2.chao long")
    print("3.banh canh")
    print("4.bun rieu")
    print("5.pho bo")
    print("=================")
    luachon=int(input("Moi nhap lua chon:"))
    print("=================")
    if luachon==1:
        print("1.hu tieu")
    elif luachon==2:
        print("2.chao long")
    elif luachon==3:
        print("3.banh canh")
    elif luachon==4:
        print("4.bun rieu")
    elif luachon==5:
        print("5.pho bo")
    else:
        print("ko hop le ")
        
def tinh_A():
    A=(32)**0.2-(1/64)**-0.25+(8/27)**(1/3)
    tinh=round(A,3)
    print(f"ket qua:{tinh}")
    return tinh
        

def can_bac():
    a=float(input("nhap a:"))
    b=float(input("nhap b:"))
    A1=((math.pow(a,1/2))-(math.pow(b,1/2)))/((math.pow(a,1/4))-(math.pow(b,1/4)))
    A2=((math.pow(a,1/2))+(math.pow(a*b,1/4)))/((math.pow(a,1/4))+(math.pow(b,1/4)))
    hieu=A1-A2                                          
if __name__=="__main__":
   menu()  
   tinh_A()
    