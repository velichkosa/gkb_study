# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и
# секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

sec= input("Введите количество секунд: ")
sec= int(sec)

hh= sec//3600
mm= (sec-((sec//3600)*3600))//60
ss= sec%60

print('%(hour)02d:%(minute)02d:%(second)02d' % {"hour":hh,"minute":mm,"second":ss})
