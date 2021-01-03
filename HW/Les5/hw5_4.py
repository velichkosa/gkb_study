"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
в новый текстовый файл."""

out_f = open('file5_4.txt', 'r', encoding = 'utf8')
content = out_f.readlines()
out_f.close()

dct = {"One":"Один", "Two":"Два", "Three":"Три", "Four":"Четыре"}

in_f = open('file5_4_1.txt', 'a', encoding = 'utf8')

for l in content:
    lst = l.split(' ')
    lst[0] = dct[lst[0]]
    in_f.write(' '.join(lst))

in_f.close()

