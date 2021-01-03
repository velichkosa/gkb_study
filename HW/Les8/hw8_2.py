"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой. """


class Zero(Exception):
    def __init__(self, txt):
        self.txt = txt


print('A / B = ?')


def division(a=int(input('Type A: ')), b=int(input('Type B: '))):
    if b == 0:
        raise Zero('Zero division error!')
    return a / b


try:
    print(division())
except Zero as error:
    print(error)
