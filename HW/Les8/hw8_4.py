"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
уроках по ООП.
"""
import json


class Off_Eq_Whouse:

    def menu():
        print('Выберите действие:\n'
              '1. Добавить новыую модель\n'
              '2. Добавить устройство на склад\n'
              '3. Просмотреть базу данных')
    pass


class Equipment(Off_Eq_Whouse):

    def __init__(self, c_name, model, eq_type, holder):
        self.c_name = c_name  # название фирмы
        self.model = model  # модель устройства
        self.eq_type = eq_type  # тип (справочник)
        self.holder = holder  # местонахождение на складе (ячейка)

    def move(self, holder):
        self.holder = holder

    def add(self, qnt):
        pass


class Printer(Equipment):
    qnt = int()

    def __init__(self, c_name, model, eq_type, cell, print_tech, dev_type, print_color, max_format):
        super().__init__(c_name, model, eq_type, cell)
        self.print_tech = print_tech
        self.dev_type = dev_type
        self.print_color = print_color
        self.max_format = max_format
        self.holder = 'whouse'
        # self.qnt = 1


    def view(self):
        with open('model.txt', 'r', encoding='utf8') as db:
            db_in = db.readlines()
        for l in db_in:
            print(l.split(','))

    def new_model(self):  # создание новой модели
        with open('model.txt', 'r', encoding='utf8') as db:
            db_in = db.readlines()
            print(len(db_in))
        mod_id = 0
        err = 0
        for l in db_in:
            if l.split(',')[2] == self.model:
                print('Такая модель существует')
                err = 1
                break
            # print(l.split(',')[0])
            if int(l.split(',')[0]) > mod_id:
                mod_id = int(l.split(',')[0])
        if err != 1:
            with open('model.txt', 'a', encoding='utf8') as db:
                db.writelines(f'{mod_id + 1},{self.c_name},{self.model}, \n')
                print(f'Добавлена новая модель!')
                return True
        else:
            return False


    def new_dev(self, mod_id):
        dev_id = 0
        with open('db.txt', 'a', encoding='utf8') as db:
            for l in db:
                # print(l.split(',')[0])
                if int(l.split(',')[0]) > dev_id:
                    dev_id = int(l.split(',')[0])
            db.writelines(f'{dev_id + 1},{mod_id},{self.holder},{self.model}, \n')
            print(f'Добавлена новая модель!')
        pass


    def cnt(self, model):  # метод подсчета количества устройств по полю model
        with open('model.txt', 'r', encoding='utf8') as db:
            db_str = db.readlines()
            cnt = 0
            for l in db_str:
                cnt = cnt + l.split(',').count('lj 1200')
        return cnt

    def __str__(self):
        return f'Инвентарный номер: {self.inv_num}\n' \
               f'Производитель: {self.c_name}\n' \
               f'Модель: {self.model}\n' \
               f'Технология печати: {self.print_tech}\n' \
               f'Тип устройства: {self.dev_type}\n' \
               f'Параметры цвета: {self.print_color}\n' \
               f'Максимальный формат: {self.max_format}\n' \
               f'Закреплен за: {self.holder}\n' \
               f''


"""думаю как добавлять устройство с такой жи моделью чтобы плюсовалось/ жсон"""


class Scanner(Equipment):
    pass

# run = Off_Eq_Whouse
# run.menu()
prin1 = Printer('HP', 'lj 1200', 'Printer', 'A2', 'laser', 'MFU', 'color', 'A4')
prin1.new_model()
prin1.move('it')
prin1.view()
