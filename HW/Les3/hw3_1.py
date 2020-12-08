# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(arg1= int(input("Input number 1:")), arg2= int(input("Input number 2:"))):
    if arg2 != 0:
        return arg1 / arg2
    else: raise ZeroDivisionError('Division by zero')

print(division())