import os
import subprocess
import re
from datetime import date, datetime
# import timeit
# Засечь время работы программы


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
    print('Current versions of the Linux kernel support four mount options, which can be specified in fstab:')
    print('strictatime (formerly atime, and formerly the default; strictatime as of 2.6.30) – always update atime, which conforms to the behavior defined by POSIX')
    print('relatime ("relative atime", introduced in 2.6.20 and the default as of 2.6.30) – only update atime under certain circumstances: if the previous atime is older than the mtime or ctime, or the previous atime is over 24 hours in the past')
    print('nodiratime – never update atime of directories, but do update atime of other files')
    print('noatime – never update atime of any file or directory; implies nodiratime; highest performance, but least compatible')
    print('lazytime – update atime according to specific circumstances laid out below')
    input('Нажмите любую клавишу для продолжения')
else:
    print("Продолжаем")

# Опции монтирования
# https://en.wikipedia.org/wiki/Stat_%28system_call%29#Criticism_of_atime
# xub@xub:~$ mount | grep " / "
#/dev/sda2 on / type ext4 (rw,relatime,errors=remount-ro)
# https://access.redhat.com/documentation/ru-ru/red_hat_enterprise_linux/6/html/power_management_guide/relatime


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

input_date = date(2023, 6, 1)

print('Input date: ', input_date)

list_output = ()
# цикл
full_size = 0
for path in list_path:
    result = subprocess.check_output('ls ' + path, shell=True)
    output = result.decode('utf-8').strip()
    list_file_in_folder = output.split()
    print()
    print(path)
    # если нет то напиши not found

    for i in list_file_in_folder:
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
        access_data_file = datetime.strptime(match, "%Y-%m-%d").date()
        print(access_data_file)

        if access_data_file < input_date:
            size_result = int(size_result)
            full_size = full_size + size_result
            print(access_data_file, 'меньше', input_date, i, size_result/1024/1024, 'Mb')
        


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

######################
# strace             #
######################