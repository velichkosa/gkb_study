# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить
# ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
# чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится
# специальный символ, выполнение программы завершается. Если специальный символ
# введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
# полученной ранее сумме и после этого завершить программу.

sum = 0

def sum_str(str, shift):
    sumnum = 0
    for num in [int(item) for item in str[0:len(str) - shift].split(' ')]:
        sumnum = sumnum + num
    return sumnum

while True:
    str = input('Type a string of numbers separated by space: ')
    if str == '!':
        break
    elif ' !' in str:
        sum= sum + sum_str(str, 2)
        print(sum)
        break
    elif '!' in str:
        sum = sum + sum_str(str, 1)
        print(sum)
        break
    else:
        sum = sum + sum_str(str, 0)
        print(sum)