import os
import subprocess
import re
from datetime import date, datetime

env_path = os.getenv("PATH")
list_path = env_path.split(':')

def count_path():
    count_file = 0
    # Выполнить команду и получить вывод
    for path in list_path:
        result = subprocess.check_output('ls ' + path + ' | wc -l', shell=True)
    # Преобразовать вывод в строку и удалить лишние пробелы
        output = result.decode('utf-8').strip()
    # Присвоить переменной значение вывода
        print('Path:', path, 'Number files:', output)
        count_file = count_file + int(output)
    print('Total file:', count_file) 
count_path()

# Функция ввода даты
# year = int(input('Enter a year: '))
# month = int(input('Enter a month: '))
# day = int(input('Enter a day: '))
# # try exept

# input_date = date(year, month, day)


input_date = date(2023, 5, 22)

print('Input date: ', input_date)

# today = datetime.date.today()
# print(today)

print()
# data_input = input()
# example data input
# дополнительная фича не позднее

list_output = ()
# цикл

for path in list_path:
    result = subprocess.check_output('ls ' + path, shell=True)
    output = result.decode('utf-8').strip()
    list_file_in_foldet = output.split()
    # print(list_file_in_foldet)
    for i in list_file_in_foldet:
        result = subprocess.check_output('stat ' + path + '/' + i, shell=True)
        output = result.decode('utf-8').strip()
        full_data = output.split('\n')
        # print(full_data)
        date = full_data[-4]
        pattern = r'\b\d{4}-\d{2}-\d{2}\b'
        match = re.findall(pattern, date)
        match = ''.join(match)
        # print(match)
        modify_data_file = datetime.strptime(match, "%Y-%m-%d").date()
        # print(modify_data_file)

        if modify_data_file < input_date:
            print(modify_data_file, 'меньше', input_date, i)

# цикл

'''
result = subprocess.check_output('stat ' + list_path[-1] + '/' + list_file_in_foldet[0], shell=True)
output = result.decode('utf-8').strip()
full_data = output.split('\n')
print(full_data[0])
print(full_data[-4])
print(full_data[-3])

print()


pattern = r'\b\d{4}-\d{2}-\d{2}\b'

match = re.findall(pattern, date)
match = ''.join(match)
# print(type(match))
'''


# ("([0-9]{4}\-[0-9]{2}\-[0-9]{2})")

# def create_list():

# step 1
# Красиво оформить
# | Отобразить красиво PATH
# | Подсчитать количество в каждам из каталогов ls | wc -l
# | Опционально из них количество ссылок

# Получить список всех файлов

# stat file 
# Проити по каждому файлу используя stat выдернув 

# В каталоге содержится такой-то устаревший file 