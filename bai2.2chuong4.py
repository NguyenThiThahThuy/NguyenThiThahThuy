# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:31:45 2024

@author: Nguyễn Thị Thanh Thùy 23704131
"""

a= float(input("Nhap a(a<>0): "))
b= float(input("Nhap b: "))
c= float(input("Nhap c: "))
delta=b**2-4*a*c
if delta < 0:
    print(" Phuong trinh vo nghiem ")
if delta == 0:
    print("Phuong trinh co nghiem kep x1=x2=,"-b/(2*a))
if delta > 0:
    print("Phuong trinh co hai nghiem phân biệt x1=",(-b+ delta**0.5)/2*a," and x2 =",(-b-delta**0.5)/2*a)
    
