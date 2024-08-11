# -*- coding: cp1251 -*-
print('Введите 5-ти значное число' )
a=float(input())

ed=a % 10
print(ed)

des=a % 100 // 10
print(des)

sot=a % 1000 // 100
print(sot)

tis=a % 10000 // 1000
print(tis)

dtis=a // 10000
print(dtis)

print(((des ** ed)*sot)/(dtis-tis))

