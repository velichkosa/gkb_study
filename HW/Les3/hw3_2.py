"""2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой."""

def user_info(name, sname, bdate, cresidence, email, pnumber):
    return (name, sname, bdate, cresidence, email, pnumber)

name = input('Type your name: '),
sname = input('Type your surname: '),
bdate = input('Type your birth date: '),
cresidence = input('Type your city of residence: '),
email = input('Type your email: '),
pnumber = input('Type your phone number: ')

date = user_info(name, sname, bdate, cresidence, email, pnumber)
print(f'{date[0]} {date[1]} born on {date[2]}, living in the city {date[3]}. e-mail: {date[4]}, phone number: {date[5]}')
