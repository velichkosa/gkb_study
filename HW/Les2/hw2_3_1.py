# 3.1
# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна,
# лето, осень). Напишите решения через list и через dict.
#-----------------------------list---------------------------------
lst=[(1,'январь', 'зима'), (2,'февраль', 'зима'), (3, 'март', 'весна'),
     (4, 'апрель', 'весна'), (5, 'май', 'весна'), (6, 'июнь', 'лето'),
     (7, 'июль', 'лето'), (8, 'август', 'лето'), (9, 'сентябрь', 'осень'),
     (10, 'октябрь', 'осень'), (11, 'ноябрь', 'осень'), (12, 'декабрь', 'зима')]
month = input("Введите месяц в числовом фомате:")

try:
    if int(month) < 1 or int(month) > 12 :
        print("Нет такого месяца!")
except ValueError:
    print("Не число или пустое значение")
else:
    for i in lst :
        if i[0] == int(month) :
            print("Число", month, "соответствует месяцу:", i[1], ", и относится к времени года:", i[2])
            break