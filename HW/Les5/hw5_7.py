"""7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если
фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней
прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста."""
from functools import reduce
import json

with open('file5_7.txt', 'r', encoding = 'utf8') as content:
    content = content.readlines()

    def profit(content):
        for i in content:
            yield i.split(' ')[0], int(i.split(' ')[2]) - int(i.split(' ')[3])

positive_prf = len([l for l in profit(content) if l[1] > 0])
result = list()
result.append(dict([l for l in profit(content)]))
result.append({"average_profit":
                   reduce(lambda l, i: l + i, [int(l[1]) for l in profit(content) if l[1] > 0])/positive_prf})

print(result)

with open('file5_7_1.json', 'w', encoding ='utf8') as out_f:
    json.dump(result, out_f)