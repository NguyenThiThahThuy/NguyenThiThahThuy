# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 18:49:43 2024

@author: Nguyễn Thị Thanh Thùy 23704131
"""
km = float(input("Nhập độ dài quãng đường đã đi(km):"))
tien = 3*13000 + 5*12000 + (km -8)*10000
if km > 1:
   print("Trả 20000 cho 1km ")
elif km == 3:
    print("Số tiền phải trả =", km * 13000)
elif 4 <= km <= 8:
    print("Số tiền phải trả =", km * 13000 + ((km-3)*12000))
elif km > 8:
    print("Số tiền phải trả =", (km*13000 + ((km-3)*12000)+((km-8)*10000)))
if tien  > 100:
    print("Số tiền cần phải trả sau cùng =", tien - (tien*0.08))
    
    

    
          
