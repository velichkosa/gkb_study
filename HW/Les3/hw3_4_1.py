"""4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде
функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции
возведения числа в степень.
Первый — возведение в степень с помощью оператора **."""

def my_func(num= float(input('Type real positive number: ')),
            deg= int(input('Type integer degree: '))):

    if deg < 0:
        return 1/(num ** abs(deg))
    if deg > 0:
        return num ** deg

print('Result of raising a number to degree: ', my_func())
