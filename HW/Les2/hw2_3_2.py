# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна,
# лето, осень). Напишите решения через list и через dict.
#-----------------------------dict---------------------------------
dct={"winter": ((1, "jan"), (2, "feb"), (12, "dec")),
     "spring": ((3, "mar"), (4, "apr"), (5, "may")),
     "summer": ((6, "jun"), (7, "jul"), (8, "aug")),
     "autumn": ((9, "sep"), (10, "oct"), (11, "nov"))}

month = input("Введите месяц в числовом фомате:")

try:
    if int(month) < 1 or int(month) > 12 :
        print("Нет такого месяца!")
except ValueError:
    print("Не число или пустое значение")
else:
    for season in dct.keys() :
        for nmonth in dct[season] :
            if nmonth[0] == int(month) :
                print("Число", month, "соответствует месяцу:", nmonth[1], ", и относится к времени года:", season)
                break