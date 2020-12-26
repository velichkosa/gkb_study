"""3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться
только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток,
соответственно. В методе деления должно осуществляться округление значения до целого числа.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных
двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух
клеток больше нуля, иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества
ячеек этих двух клеток.

Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление
количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному
аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет
строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет
строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке."""


class Cell:
    def __init__(self, val):
        self.val = val

    def make_order(self, c_in_row = 5):
        cnt = 0
        cell_str = str()
        while cnt < self.val:
            if (cnt % c_in_row) == 0 and cnt != 0:
                cell_str = cell_str + '/n'
            cell_str = cell_str + '*'
            cnt += 1
        return cell_str

    def __add__(self, other):
        return Cell(self.val + other.val)

    def __sub__(self, other):
        if self.val - other.val < 0:
            return 'Разность количества ячеек двух клеток меньше нуля'
        else:
            return Cell(self.val - other.val)

    def __mul__(self, other):
        return Cell(self.val * other.val)

    def __floordiv__(self, other):
        return Cell(self.val // other.val)

    def __str__(self):
        return f'{self.make_order()}'


cell = Cell

print(f'floordev: {cell(195) // cell(21)} \n'
      f'add: {cell(10) + cell(17)} \n'
      f'sub: {cell(24) - cell(17)} \n'
      f'sub_err: {cell(24) - cell(41)} \n'
      f'mul: {cell(5) * cell(7)}')