# 4
# Пользователь вводит целое положительное число. Найдите самую большую цифру
# в числе. Для решения используйте цикл while и арифметические операции.

inum= input("Введите целое положительное число: ")
inum= str(inum)
x= 0
compare= 0

while x<= len(inum)-1:
    if int(inum[x]) > int(compare):
        compare= inum[x]
        idx= x
    x= x+1

print("Наибольшая цифра=", compare, ", её индекс: ", idx)