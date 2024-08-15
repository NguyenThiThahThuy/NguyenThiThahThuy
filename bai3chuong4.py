# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:56:04 2024

@author: Nguyễn Thị Thanh Thùy 23704131
""" 
    
a = float(input("Nhập độ dài cạnh a: "))
b = float(input("Nhập độ dài cạnh b: "))
c = float(input("Nhập độ dài cạnh c: "))
if a == b == c:
    print("Tam giac deu ")
elif a == b or b == c or c == a:
    print("Tam giac can ")
elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
    print("Tam giac vuong can")
elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
    print("Tam giac vuong")
else:
    print("Tam giac thuong")

          