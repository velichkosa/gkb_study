"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать
их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например,
месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных."""

class Data:
    def __init__(self, d_string):
        self.d_string = d_string

    @classmethod
    def pars1(cls, date: 'Data'):
        lst = [int(date.d_string.split('-')[0]), int(date.d_string.split('-')[1]), int(date.d_string.split('-')[2])]
        return lst

    @staticmethod
    def valid(date: 'Data'):
        month_day = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        p_date = date.d_string.split('-')
        if int(p_date[1]) > 12:
            raise ValueError('Month error')
        if int(p_date[0]) > month_day.get(int(p_date[1])):
            raise ValueError('Day error')
        if len(p_date[2]) not in {2, 4}:
            raise ValueError('Year error')
        print('Validation successful')

date = Data('28-02-20')
print(date.pars1(date))
date.valid(date)