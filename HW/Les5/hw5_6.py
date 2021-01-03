"""6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно,
чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий
название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"""

f_out = open('file5_6.txt', 'r',  encoding = 'utf8')
content = f_out.readlines()
f_out.close()

def pars(str_lst):
    cnt = 0
    while cnt < len(str_lst):
        name = str_lst[cnt].split(':')[0]
        hrstr =  str_lst[cnt].split(':')[1]
        new_hr = str()
        for l in hrstr:
            try:
                l = int(l)
            except:
                if l != ' ':
                    new_hr = new_hr + ''
                else: new_hr = new_hr + ' '
            else:
                new_hr = (new_hr + str(l))
        new_hr = new_hr.split(' ')
        new_hr = [int(l) for l in new_hr if l != '']
        cnt += 1
        yield name, sum(new_hr)

dct = dict([l for l in pars(content)])
print(dct)
