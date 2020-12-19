""" 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов."""

arg = input('Type value for argument: ')
arg = arg.split()
arg = [int(l) for l in arg]

def my_func(arg1):
    return sum(arg1) - min(arg1)

print(my_func(arg))