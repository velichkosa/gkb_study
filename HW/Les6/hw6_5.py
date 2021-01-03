"""5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title
(название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три
дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать
переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра."""


class Stationery:

    def __init__(self, title):
        self.title = title

    def _draw(self):
        print('Запуск отрисовки.')
        pass

    def __call__(self, *args, **kwargs):
        self._draw();


class Pen(Stationery):
    def _draw(self):
        print(f'Инструмент {self.title}. Запуск отрисовки.')


class Pencil(Stationery):
    def _draw(self):
        print(f'Инструмент {self.title}. Запуск отрисовки чертежа.')


class Handle(Stationery):
    def _draw(self):
        print(f'Инструмент {self.title}. Запуск.')

pen = Pen('Ручка')
pen()

pencil = Pencil('Карандаш')
pencil()

handle = Handle('Маркер')
handle()