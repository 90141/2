# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


print('解一元二次方程式')

a=int(input('請輸入a:'))
b=int(input('請輸入b:'))
c=int(input('請輸入c:'))

x=(-b+((b**2)-(4*a*c)**0.5))/(2*a)
y=(-b+((b**2)+(4*a*c)**0.5))/(2*a)

print('解為:',x,y)