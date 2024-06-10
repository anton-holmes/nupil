import os
import subprocess
import re
from datetime import date, datetime
# import timeit
# Засечь время работы программы
# Использовать данные предыдущего анализа или собрать заново

env_path = os.getenv("PATH")
list_path = env_path.split(':')
# list_path.append('/opt')
# print(list_path)

# Программа предназначена, выберите режим
print('####################################')
print('###########    NUPIL   #############')
print('####################################')

print(r"¯\_(ツ)_/¯", 'nupil - предназначен для поиска неиспользуемых или последних исполняемых файлов в *nix операцтонных системах')
print()
input('Нажмите любую клавишу для продолжения')
print('++++++++++++++++++++++++++++++++++')

print()
print('Ваш режим доступа к дискам')
mode = subprocess.check_output('mount | grep " / "', shell=True)
output = mode.decode('utf-8').strip()
print(output)
print()
print('++++++++++++++++++++++++++++++++++')

user_input = input("Введите 'a' или 'A' для получения справки о режимах доступа к дискам: ")
if user_input.upper() == 'A':
    print("Опции монтирования дисков")
else:
    print("Продолжаем")


# Вернуться к предыдущему шагу 
# Выход

print()
print('Каталоги PATH и количество исполняемых файлов в них')
def count_path():
    count_file = 0
    # Выполнить команду и получить выводq
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
    print('/opt',)
    print('++++++++++++++++++++++++++++++++++')
    input('Нажмите любую клавишу для продолжения')
else:
    print("Продолжаем")

# Выберите режим использования
# today = datetime.date.today()
# print(today)

print()

# поиск всех файлов и их зависимостей, сколько занимают памяти
# зависимости apt-cache depends имя_пакета
# ldd /абсолютный путь к файлу
# apt-cache depends --recurse --no-recommends --no-suggests --no-conflicts --no-breaks --no-replaces --no-enhances mc | grep "^\w" | sort -u
# в результате выполнения этой команды будет выведен список уникальных зависимостей пакета Midnight Commander без рекомендаций, предложений, конфликтов, нарушений, замен и улучшений, отсортированный в алфавитном порядке.

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
# synaptik
# менеджер пактов dpkg

# Находит все файлы программы
# whereis libreoffice
# 

#Находит все файлы по названию 
# find
#locate libreoffice

# ищет где лежат файлы пакета
# dpkg-query -L kontena-lens 

# Выводит все файлы 

# Функция ввода даты
# year = int(input('Enter a year: '))
# month = int(input('Enter a month: '))
# day = int(input('Enter a day: '))
# # try exept
# input_date = date(year, month, day)

input_date = date(2022, 6, 1)

print('Вывести все исполняемые файлы обращение к которым производилось старше : ', input_date)

list_output = ()
# цикл
full_size = 0
t =  {}
for path in list_path:
    result = subprocess.check_output('ls ' + path, shell=True)
    output = result.decode('utf-8').strip()
    list_file_in_folder = output.split()
    # print()
    # print(path)
    # если нет то напиши not found
    # Здесть ожидание с
    for i in list_file_in_folder:
        result = subprocess.check_output('stat ' + path + '/' + i, shell=True)
        output = result.decode('utf-8').strip()
        full_data = output.split('\n')
        # print(full_data[0]) # BIN + СИМВОЛЬНАЯ ССЫЛКА 

        size = subprocess.check_output('whereis ' + path + '/' + i, shell=True)
        size_output = size.decode('utf-8').strip()
        

        zise_all_path = re.findall(r'/(.*)$', size_output)
        zise_all_path = ''.join(zise_all_path)
        size_sum = subprocess.check_output('du -csh ' + '/' + zise_all_path, shell=True)
        size_output = size_sum.decode('utf-8').strip()
        # print(size_output.split()[-2]) # ИТОГО

        # print('++++++++++++++++++++')

        # Это могут быть символьные ссылки, которые и содержат факт 
        # если символьная ссылка существует в другом каталоге, если в этом то просчитать другой 
        # и его пропустить

        name = full_data[0]
        date = full_data[-4]
        pattern = r"\b\d{4}-\d{2}-\d{2}\b"
        match = re.findall(pattern, date)
        match = ''.join(match)
        access_data_file = datetime.strptime(match, "%Y-%m-%d").date()

        # # print(str(access_data_file), i) 

        t.update({name: {'data':str(access_data_file) , 'size': size_output.split()[-2], 'path_folder': path}})
print(t)



        # name i, size MB, datatime, data  

        # if access_data_file < input_date:
        #     size_result = int(size_result)
        #     full_size = full_size + size_result
        #     print(access_data_file, 'меньше', input_date, i, size_result/1024/1024, 'Mb')
        # du -sh .
input('Нажмите любую клавишу для продолжения')       


        # found_matching_data = False

        # for z, access_data_file in enumerate(i):
        #     if access_data_file < input_date:
        #         size_result = int(size_result)
        #         full_size = full_size + size_result
        #         print(access_data_file, 'меньше', input_date, z, size_result/1024/1024, 'Mb')
        #         found_matching_data = True

        # if not found_matching_data:
        #     print('Не найдено')
            # округлить до 5 знаков после запятой
        

# Результат вывода размера файла и зависимостей может быть несовсем точным т.к.
# существуют каталолги где где храняться в ОС Linux где храняться временный файлы 
# или файлы имеюющие наибеольшую частоту изменений

######################33
# Вывод списка старше определенной даты
# Вывод списка зависимостей и зависимости зависимостей
# Вывод man 
# strace
# Рекомендации по удалению
# Не забудь snap
#########################

# print(full_size/1024/1024, 'Mb')
# print(r"¯\_(ツ)_/¯")

t='#'
for i in range(10):
    t = t+'#'
    print(t)

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

# какому менеджеру пакетов принадлежит программа
# зависящие пакеты, зависимые пакеты
# example data input

'''
Опция `relatime` (от "relative atime") используется в Linux-системах для управления обновлением времени доступа (atime) к файлам на файловой системе. Вот более подробное объяснение того, как работает `relatime`:

1. **Оптимизация обновления времени доступа**: По умолчанию, в Unix-подобных системах, каждый раз, когда файл читается, время его последнего доступа (atime) обновляется. Это может привести к лишним операциям записи на диск, что замедляет работу системы, особенно на файловых системах с большим количеством операций ввода-вывода.

2. **Условия обновления atime с `relatime`**: Когда опция `relatime` установлена, время доступа к файлу будет обновляться только в следующих случаях:
   - Если предыдущее время доступа (atime) старше времени изменения (mtime) или времени создания (ctime) файла.
   - Если предыдущее время доступа (atime) отстоит более чем на 24 часа назад от текущего времени.
'''
