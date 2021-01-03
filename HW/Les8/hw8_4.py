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

class Equipment():

    def __init__(self, c_name, model, sn):
        self.c_name = c_name  # название фирмы
        self.model = model  # модель устройства
        self.sn = sn
        self.holder = None  # местонахождение

    def _move(self, holder):
        self.holder = holder

    def add(self, qnt):
        pass

class Whouse:
    def __init__(self, max_volume):
        self.max_volume = max_volume
        self.total = 0
        self.storage = {'printers': set()}
        self.add_mapper = {Printer: 'printers'}


    def get_tech_to_whouse(self, equip: Equipment):
        if self.total == self.max_volume:
            raise OverflowError('Склад заполнен!')
        self.storage[self.add_mapper[type(equip)]].add(equip)
        print(type(equip))
        equip._move('whouse')
        self.total += 1

    def move_holder(self, tech_type, holder):
        print(self.storage[tech_type] )
        tech_to_holder = self.storage[tech_type].pop()
        tech_to_holder._move(holder)
        self.total -= 1

    def __call__(self, *args, **kwargs):
        self.get_tech_to_whouse(*args, **kwargs)

class Printer(Equipment):
    def __init__(self, c_name, model, sn, ptype, color):
        super().__init__(c_name, model, sn)
        self.ptype = ptype
        self.color = color

    def add(self):
        return f'Company: {self.c_name} Model: {self.model} s/n {self.sn} Paper type: {self.ptype} ' \
               f'Color: {self.color} Holder: {self.holder}'

    def __call__(self, *args, **kwargs):
        self.add()

    def __str__(self):
        return f'Company: {self.c_name}\nModel: {self.model}\ns/n {self.sn}\nPaper type: {self.ptype}\n' \
               f'Color: {self.color}\nHolder: {self.holder}'

printer1 = Printer('hp', 'lj 1100', '1212223', 'A4', 'BW')
printer2 = Printer('hp', 'lj 1100', '1212224', 'A4', 'BW')
printer3 = Printer('hp', 'lj 1100', '1212225', 'A4', 'BW')
printer4 = Printer('hp', 'lj 1100', '1212226', 'A4', 'BW')
printer5 = Printer('hp', 'lj 1100', '1212223', 'A4', 'BW')
"""Почему set() не отрабатывает? 1 и 5 одинаковые"""

warehouse = Whouse(5)
print(warehouse.total)
warehouse.get_tech_to_whouse(printer1)
warehouse.get_tech_to_whouse(printer2)
warehouse.get_tech_to_whouse(printer3)
warehouse.get_tech_to_whouse(printer4)
warehouse.get_tech_to_whouse(printer5)
warehouse.move_holder('printers', 'IT')
"""как в данном примере переместить printer3, а не последний созданный?"""

print(warehouse.total)
print(printer1)
print(printer2)
print(printer3)
print(printer4)
print(printer5)

