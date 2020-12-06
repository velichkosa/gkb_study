# 5
# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
# с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

print("-----RATING LIST-----")
rtg = [7, 5, 3, 3, 2]
while True:
    num = input("Insert new rating element (type 'end' to stop)")
    if num == 'end':
        break
    try :
        rtg.index(int(num))
    except ValueError:
        try:
            num = int(num)
            print("Will be added new value: ", int(num))
        except ValueError:
            print("ValError")
            continue
        for i in rtg:
                if rtg.index(i) + 1 == len(rtg) and num < 1:
                    rtg.insert(rtg.index(i) + 1, num)
                    print("index new el: ", rtg.index(i) + 1)
                    print(rtg)
                    break
                if num <= i:
                    continue
                else:
                    rtg.insert(rtg.index(i), num)
                    print("index new el: ", rtg.index(i) - 1)
                    print(rtg)
                    break
    else:
        rtg.insert(rtg.index(int(num)) + rtg.count(int(num)), int(num))
        print("Succses. Index of element is: ", rtg.index(int(num)) + rtg.count(int(num)) - 1)
        print(rtg)

# Такое чувство, что намутил много лишнего
# Если не важен павильный индекс вводимого числа, можно было бы делать .append и на вывод .sort(reverse=True)
