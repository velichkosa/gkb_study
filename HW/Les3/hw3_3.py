# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(arg1= int(input('Type value for argument #1: ')),
            arg2= int(input('Type value for argument #2: ')),
            arg3= int(input('Type value for argument #3: '))):

    l= [arg1, arg2, arg3]
    big1= int()
    big2= int()

    for i in l:
        if i > big1:
            big1= i
    l.pop(l.index(big1))

    for i in l:
        if i > big2:
            big2= i
    l.pop(l.index(big2))

    return big1+big2

print(my_func())