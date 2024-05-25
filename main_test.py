import os
import subprocess
import re
from datetime import date, datetime
# import timeit
# Засечь время работы программы


env_path = os.getenv("PATH")
list_path = env_path.split(':')

# Программа предназначена, выберите режим
print('nupil - предназначена для поиска неиспользуемых или последних исполняемых файлов в *nix операцтонных системах')
print(r"¯\_(ツ)_/¯")
input('Нажмите любую клавишу для продолжения')
print('++++++++++++++++++++++++++++++++++')

print()
print('Общие сведения об исполняемых файлах')
def count_path():
    count_file = 0
    # Выполнить команду и получить вывод
    for path in list_path:
        result = subprocess.check_output('ls ' + path + ' | wc -l', shell=True)
    # Преобразовать вывод в строку и удалить лишние пробелы
        output = result.decode('utf-8').strip()
    # Присвоить переменной значение вывода
        print('Path:', path, '|', 'Number files:', output)
        count_file = count_file + int(output)
    print('Total file:', count_file) 
count_path()
print()

user_input = input("Введите 'a' или 'A' для получения справки о предназначении каталогов переменной PATH, или любую другую клавишу для продолжения: ")

# ДОБАВЬ ПРОБЕЛЫ "{:<8}"
if user_input.upper() == 'A':
    print("Справка по предназначению стандартных катологов в PATH. ")
    print('++++++++++++++++++++++++++++++++++')
    print('/bin', ' - содержит исполняемые бинарные файлы различных служб, доступные для запуска любым пользователям')
    print('/sbin', ' - содержит исполняемые бинарные файлы для системного администрирования (и другие команды предназначенные для root), /sbin содержит двоичные файлы, необходимые для загрузки, восстановления и/или восстановления системы в дополнение к двоичным файлам в /bin.')
    print('/usr/bin', )
    print('/usr/sbin',)
    print('/usr/local/bin',)
    print('/usr/local/sbin',)
    print('++++++++++++++++++++++++++++++++++')
    input('Нажмите любую клавишу для продолжения')
else:
    print("Продолжаем")


# Выберите режим использования

# today = datetime.date.today()
# print(today)

print()
# example data input
# дополнительная фича не позднее
# используемые вчера 
# используемые в течении недели
# Показать самые большие пакеты
# нужно усзнать куда что устанавливают пакеты на примере libreoffice
# libreoffice --calc
# если  это 
# скольк о места занимает du -csh /lib/python3.13
# список зависимосте ldd /usr/bin/python3 
# strace /usr/bin/libreoffice отслеживание системных вызовов
# /opt 
# /user/share лежат данные /etc конфигурация

# Находит все файлы программы
# whereis libreoffice
# 

#Находит все файлы по названию 
# find
#locate libreoffice

# Выводит все файлы 


# Функция ввода даты
# year = int(input('Enter a year: '))
# month = int(input('Enter a month: '))
# day = int(input('Enter a day: '))
# # try exept

# input_date = date(year, month, day)


input_date = date(2022, 5, 25)

print('Input date: ', input_date)

list_output = ()
# цикл
full_size = 0
for path in list_path:
    result = subprocess.check_output('ls ' + path, shell=True)
    output = result.decode('utf-8').strip()
    list_file_in_foldet = output.split()
    print()
    print(path)
    # если нет то напиши not found
    for i in list_file_in_foldet:
        result = subprocess.check_output('stat ' + path + '/' + i, shell=True)
        output = result.decode('utf-8').strip()
        full_data = output.split('\n')
        # print(full_data)
        date = full_data[-4]
        size = full_data[1]
        size = size.split(' ')
        size_result = size[3]
        
        # print(date)
        
        pattern = r"\b\d{4}-\d{2}-\d{2}\b"
        match = re.findall(pattern, date)
        match = ''.join(match)
        # print(match)
        acsess_data_file = datetime.strptime(match, "%Y-%m-%d").date()
        # print(modify_data_file)

        if acsess_data_file < input_date:
            size_result = int(size_result)
            full_size = full_size + size_result
            print(acsess_data_file, 'меньше', input_date, i, size_result/1024/1024, 'Mb')
            # округлить до 5 знаков после запятой

print(full_size/1024/1024, 'Mb')
print(r"¯\_(ツ)_/¯")

# цикл
# зависимости
# краткая справка MAN
# СПРАВКА ИЗ ИНТЕРНЕТА
# рекомендации по удалению

# for i in tqdm(range(10)):
#     sleep(3)

# stat file 
# Проити по каждому файлу используя stat выдернув 
# В каталоге содержится такой-то устаревший file 