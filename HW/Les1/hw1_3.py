  # 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
  # Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n= input("Введите число n: ")
cnt1= int(n)
cnt2= int(n+n)
cnt3= int(n+n+n)

cnt=cnt1+cnt2+cnt3

print("Результат=", cnt, type(cnt))