"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов
TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат."""
from random import randint


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def __call__(self, *args, **kwargs):
        self.go()
        self.show_speed()
        self.turn(randint(0, 2))

    def go(self):
        print(f'Машина {self.name} начала движение.')

    def turn(self, direction):
        dct_turn = {0: 'право', 1: 'лево', 2: False}
        dct_turn = dct_turn.get(direction)
        if dct_turn != False: print(f'Машина повернула на {dct_turn}')

    def show_speed(self):
        cur_speed = randint(10, self.speed)
        if cur_speed > 90 and self.is_police == False and self.speed < 250:  # как определить SportCar в условии?
            print(f'Текущая скорость {cur_speed}. ПРЕВЫШЕНИЕ!!!')
        else:
            print(f'Текущая скорость {cur_speed}.')

    def stop(self):
        print('Машина остановилась.')


class TownCar(Car):
    def show_speed(self, cruise_speed):
        cur_speed = randint(cruise_speed, self.speed)
        if cur_speed > 60:
            print(f'Текущая скорость {cur_speed}. ПРЕВЫШЕНИЕ!!!')
        else:
            print(f'Текущая скорость {cur_speed}.')


class SportCar(Car):
    def race(self):
        trc_dct = {0: 'На трэке', 1: 'Пробный заезд'}
        track_factor = randint(0, 1)
        print(f'{trc_dct.get(track_factor)}')


class WorkCar(Car):
    def show_speed(self, cruise_speed):
        cur_speed = randint(cruise_speed, self.speed)
        if cur_speed > 40:
            print(f'Текущая скорость {cur_speed}. ПРЕВЫШЕНИЕ!!!')
        else:
            print(f'Текущая скорость {cur_speed}.')


class PoliceCar(Car):
    def pursuit(self):
        prs_dct = {0: 'Патрулирование', 1: 'Преследование'}
        prs_factor = randint(0, 1)
        print(f'{prs_dct.get(prs_factor)}')


tc = TownCar(90, 'Black', 'Buick', False)
wc = WorkCar(80, 'Yellow', 'MAN', False)
sc = SportCar(390, 'Red', 'Pagani Zonda', False)
pc = PoliceCar(190, 'Blue', 'Lada', True)

tc.go(), tc.show_speed(40), tc.turn(randint(0, 2))
print('----------------------------------------')
wc.go(), wc.show_speed(40), wc.turn(randint(0, 2)), wc.stop()
print('----------------------------------------')
sc.race(), sc()
print('----------------------------------------')
pc.pursuit(), pc()
