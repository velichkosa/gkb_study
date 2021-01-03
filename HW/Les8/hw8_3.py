"""3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить
работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список. Класс-исключение
должен контролировать типы данных элементов списка.

Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.

Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. При
этом работа скрипта не должна завершаться."""


class Not_num(Exception):
    def __init__(self, txt):
        self.txt = txt


def list_num():
    num_str = list()
    while True:
        try:
            num = input('Type number: ')
            if num == 'stop': break
            if num.isdigit() == False:
                raise Not_num("It's not num!")
            num_str.append(num)
        except Not_num as error:
            print(error)
    return num_str


print(list_num())
