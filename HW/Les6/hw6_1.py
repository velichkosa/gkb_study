"""1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running
(запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго
(желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно
осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав
экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
сообщение и завершать скрипт."""

from itertools import cycle, count
from time import sleep

class TrafficLight:
    color = ['red', 'yellow', 'green']

    def __init__(self):
        if TrafficLight.color[0] != 'red':
            err = 'Color error'
            return err
        elif TrafficLight.color[1] != 'yellow':
            err = 'Color error'
            return err
        elif TrafficLight.color[2] != 'green':
            err = 'Color error'
            return err

    def running(self, col):
        timer = {'red': 7, 'yellow': 2, 'green': 5}
        print(f'{TrafficLight.color[col].upper()}, {timer.get(TrafficLight.color[col])} sec')
        for l in count(-timer.get(TrafficLight.color[col]), 1):
            if l > -1 : break
            print(-l)
            sleep(1)

try:
    tl = TrafficLight()
except:
    print('TrafficLight is broken!')
else:
    for l in cycle([0, 1, 2]):
        tl.running(l)
