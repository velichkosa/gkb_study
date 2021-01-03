"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет
количества строк, количества слов в каждой строке."""

out_f = open("file5_2.txt", "r")
content = out_f.readlines()
out_f.close()

print(f'String count: {len(content)}')
for l in enumerate(content):
    print(f'String #{l[0]+1}, word count: {len(l[1].split(" "))}')
