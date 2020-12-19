"""Второй — более сложная реализация без оператора **, предусматривающая использование цикла."""

def my_func(num= float(input('Type real positive number: ')),
            deg= int(input('Type integer number: '))):
    cnt = 0
    res = num
    if deg < 0:
        while cnt != abs(deg)-1:
            res= res*num
            cnt += 1
        return 1/res
    if deg > 0:
        while cnt != deg - 1:
            res = res * num
            cnt += 1
        return res

print('Result of raising a number to degree: ', my_func())