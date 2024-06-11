import os
import sys
import subprocess
import re
import time
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

print(r"¯\_(ツ)_/¯", 'nupil - предназначен для поиска неиспользуемых или последних исполняемых файлов в *nix операционных системах')
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
    print('/bin', ' - Директория предназначена для хранятся основных исполняемых файлов, необходимых для минимальной загрузки и функционирования ОС. Данные файлы включают в себя утилиты командной строки, необходимые для  работы системы, к примеру для работы с файловой системой, команды для управления процессами и др.')
    print('++++++++++++++++++++++++++++++++++')
    print('/sbin', ' - В директории хранятся системные исполняемые файлы, которые используются для администрирования и управления системой. Выполнение представленных файлов обычно требуют повышенных привилегий (как правило, root). Могут быть использованы на ранних стадиях загрузки системы или для восстановления после сбоев, монтирования файловых систем, настройки сети, администрирования учетных записей и др.')
    print('++++++++++++++++++++++++++++++++++')
    print('/usr/bin', ' - Директория предназначена для хранятся основных исполняемых файлов и пользовательских программ и представляют собой утилиты и приложения, которые используются пользователями системы. В отличие от /bin, содержимое /usr/bin не является необходимым для загрузки или функционирования базовой системы.')
    print('++++++++++++++++++++++++++++++++++')
    print('/usr/sbin', ' - В директории хранятся системные исполняемые файлы, которые также предназначены для администрирования и управления, но они обычно не являются критически важными для базового функционирования. Данные файлы могут быть установлены отдельно от основной системы и предназначены для использования системными администраторами. В качестве примера в данный каталог включены утилиты для управления службами, настройки безопасности и др.')
    print('++++++++++++++++++++++++++++++++++')
    print('/usr/local/bin', ' - Директория предназначена для хранения исполняемых файлов и пользовательских программ, которые не входят в стандартный набор поставляемых с ОС. Обычно в данную директорию располагают программы, которые не устанавливаются с помощью пакетных менеджеров, а компилируются и устанавливаются вручную или с помощью сторонних инструментов установки. Файлы расположенные в /usr/local/bin доступны всем пользователям системы.' )
    print('++++++++++++++++++++++++++++++++++')
    print('/usr/local/sbin', ' - Данная директория аналогична /usr/local/bin, но предназначена для хранения системных исполняемых файлов пользовательских программ, которые требуют повышенных привилегий для выполнения. Эти файлы также не входят в стандартный набор поставляемых с ОС и устанавливаются вручную или с помощью других инструментов установки. Файлы в `/usr/local/sbin` обычно доступны только администраторам системы.')
    print('++++++++++++++++++++++++++++++++++')
    print('/opt', '- в данной директории располагаются дополнительные пакеты. Например при установке программы из deb пакета, в каталоги перечисленные выше помещается файл ссылающийся на исходный код, который располагается в /opt.')
    print('++++++++++++++++++++++++++++++++++')
    input('Нажмите любую клавишу для продолжения')
else:
    print("Продолжаем")
print()

input_date = date(2022, 6, 1)

print('Для определяния неспользуемых бинарных файлов введите ДАТУ, старше которой произвести сканирование : ', input_date)
####
#
####

list_output = ()
# цикл
full_size = 0
t, t_sort =  {}, {}
list_data, list_small_data = [], []
list_small_data_test = []
k = 0

for path in list_path:
    result = subprocess.check_output('ls ' + path, shell=True)
    output = result.decode('utf-8').strip()
    list_file_in_folder = output.split()
    z = 0
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

        t.update({name: {'data': access_data_file, 'size': size_output.split()[-2], 'path_folder': path}})

        list_data.append([name, str(access_data_file), size_output.split()[-2], path])
        
        if access_data_file < input_date:
            # list_small_if_data
            z = z + 1
            # print(1)
            list_small_data.append([name, str(access_data_file), size_output.split()[-2], path])
    list_small_data_test.append([path, z])

# Последний элемент
# print(list_data)
# print(list_data[0][-1])

print(list_small_data_test)
print(len(list_small_data))

# for i in len(list_data):
#     if list_data[0][-1] == '/usr/sbin':
#         print(list_data[i])

# while  
    # print(path, (access_data_file))
    # t_sort.update({name: {'data': str(access_data_file), 'size': size_output.split()[-2], 'path_folder': path}})
# print('path_folder' in t_sort)
# print(list_data)
# print(t.values('path_folder', path))


# print(t.values())
# print(t_sort)


# total = 1000 # total number to reach
# bar_length = 50  # should be less than 100
# for i in range(total+1):
#     percent = 100.0*i/total
#     sys.stdout.write('\r')
#     sys.stdout.write("Process: [{:{}}] {:>3}"
#                     .format('#'*int(percent/(100.0/bar_length)), bar_length, ''))
#                     # .format('#'*int(percent/(100.0/bar_length)), bar_length, int(percent)))
#     sys.stdout.flush()
#     time.sleep(0.001)


print("Сканирование успешно выполнено")

print('Вывод статистики')

print("Для просмотра результатов соответсвующих каталогов введите его путь. Например '/usr/sbin' ")


# поиск точного совпадения с существующим пакетом в apt
# dpkg --get-selections | grep -v deinstall | grep -w dc


print("Для дополнительной информации о пакете введите его название. Или Перейдите в меню выше ")



# print(t)
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


########################
# Вывод списка старше определенной даты
# Вывод списка зависимостей и зависимости зависимостей
# Вывод man man -f ls
# strace
# Рекомендации по удалению
# Не забудь snap
#########################


# print(full_size/1024/1024, 'Mb')
# print(r"¯\_(ツ)_/¯")

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

# ldd /абсолютный путь к файлу

# Выберите режим использования
# today = datetime.date.today()
# print(today)
# поиск всех файлов и их зависимостей, сколько занимают памяти
# зависимости apt-cache depends имя_пакета

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

'''
Опция `relatime` (от "relative atime") используется в Linux-системах для управления обновлением времени доступа (atime) к файлам на файловой системе. Вот более подробное объяснение того, как работает `relatime`:

1. **Оптимизация обновления времени доступа**: По умолчанию, в Unix-подобных системах, каждый раз, когда файл читается, время его последнего доступа (atime) обновляется. Это может привести к лишним операциям записи на диск, что замедляет работу системы, особенно на файловых системах с большим количеством операций ввода-вывода.

2. **Условия обновления atime с `relatime`**: Когда опция `relatime` установлена, время доступа к файлу будет обновляться только в следующих случаях:
   - Если предыдущее время доступа (atime) старше времени изменения (mtime) или времени создания (ctime) файла.
   - Если предыдущее время доступа (atime) отстоит более чем на 24 часа назад от текущего времени.
'''
