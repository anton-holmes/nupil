# import time
# import sys

# total = 1007  # total number to reach
# bar_length = 30  # should be less than 100
# for i in range(total+1):
#     percent = 100.0*i/total
#     sys.stdout.write('\r')
#     sys.stdout.write("Completed: [{:{}}] {:>3}%"
#                      .format('='*int(percent/(100.0/bar_length)),
#                              bar_length, int(percent)))
#     sys.stdout.flush()
#     time.sleep(0.002)


 #  print ("{:<8} {:<15} {:<10} {:<10}".format(k, lang, perc, change)



# ТАБЛИЦА
'''
data = [
    ["Alice", 24, "Engineer"],
    ["Bob", 30, "Developer"],
    ["Charlie", 27, "Designer"]
]

# Функция для вывода данных в виде таблицы
def print_table(data):
    # Находим максимальную длину для каждого столбца
    col_widths = [max(len(str(item)) for item in col) for col in zip(*data)]
    
    # Вывод заголовков столбцов
    headers = ["Name", "Age", "Occupation"]
    print(" | ".join(headers))
    
    # Вывод разделителя
    print("-" * (sum(col_widths) + 3 * (len(headers) - 1)))
    
    # Вывод данных
    for row in data:
        print(" | ".join(str(item).ljust(width) for item, width in zip(row, col_widths)))

# Вывод данных в виде таблицы
print_table(data)
'''
import time
import os

file_stat = os.stat("/usr/bin/ls")
atime = file_stat.st_atime
atime_str = time.strftime('%Y-%m-%d %H:%N:%S', time.localtime(atime))

print(atime_str)

