"""6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите
внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть
условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа
10 завершаем цикл. Во втором также необходимо предусмотреть условие, при котором
повторение элементов списка будет прекращено."""

from itertools import cycle, count
from time import sleep

lst = list()
print('итератор, генерирующий целые числа, начиная с указанного,')
for l in count(3, 1):
    if l > 10: break
    print(l)
    lst.append(l)
    sleep(0.5)

print('итератор, повторяющий элементы некоторого списка, определенного заранее.')
cnt = 0
for l in cycle(lst):
    if cnt > 20:
        break
    sleep(0.5)
    print(l)
    cnt += 1
