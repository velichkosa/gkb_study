"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
средней величины дохода сотрудников."""

from functools import reduce

out_f = open('file5_3.txt', 'r')
content = out_f.readlines()
out_f.close()

def get_less_than(db, pval):
    for l in enumerate(db):
        if int(l[1].split('/')[1]) < pval: print(l[1].split('/')[0])

def mid_sal (db):
    salary = list()
    for l in enumerate(content):
        salary.append(int(l[1].split('/')[1]))
    return reduce(lambda x,y: x + y, salary)/len(salary)

print('Salary less them 20 000 at:')
get_less_than(content, 20000)
print(f'Average income: {mid_sal(content)}')
