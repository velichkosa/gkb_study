"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

from random import randint
from functools import reduce

in_f = open('file5_5.txt', 'w+')
in_f.write(' '.join([str(randint(1, 10)) for i in range(20)]))
in_f.seek(0)
content = in_f.readline()
in_f.close()

print(reduce(lambda x,y: int(x) + int(y), content.split(' ')))
