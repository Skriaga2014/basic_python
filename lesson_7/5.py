'''
4. Написать скрипт, который выводит статистику для заданной папки в виде
словаря, в котором ключи — верхняя граница размера файла (пусть будет
кратна 10), а значения — общее количество файлов (в том числе и в подпапках),
размер которых не превышает этой границы, но больше предыдущей (начинаем с 0),
например:

    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }

Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000
байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

5. *(вместо 4) Написать скрипт, который выводит статистику для заданной папки
в виде словаря, в котором ключи те же, а значения — кортежи вида
(<files_quantity>, [<files_extensions_list>]), например:

    {
      100: (15, ['txt']),
      1000: (3, ['py', 'txt']),
      10000: (7, ['html', 'css']),
      100000: (2, ['png', 'jpg'])
    }

Сохраните результаты в файл <folder_name>_summary.json в той же папке,
где запустили скрипт.
'''

# принимает число, возвращает округление до (10 ** x) в большую сторону
def get_round_size(path):
    size = os.path.getsize(path)
    if size == 0:
        size_round = 0
    elif size == 1:
        size_round = 10
    else:
        size_round = 10 ** len(str(size))
        if size == size_round / 10:
            size_round = size

    ext = os.path.splitext(path)[-1]
    return size_round, ext


import os
import json

# path = выбранная папка
start_path = os.path.join(os.getcwd(), '../')

temp_list = os.walk(start_path)
temp_list = ((os.path.join(i[0], m) for m in i[-1]) for i in temp_list if len(i[-1]) > 0)

path_list = []
[path_list.extend(i) for i in temp_list]

dict_size = {}
for path in path_list:
    round, ext = get_round_size(path)
    if round in dict_size:
        dict_size[round][0] += 1
        dict_size[round][1].append(ext)
    else:
        dict_size[round] = [1, [ext]]

for item in sorted(dict_size):
    dict_size[item] = (dict_size[item][0], list(set(dict_size[item][1])))
    print(f'{item}: {dict_size[item]}')

with open(os.path.join(start_path, '_summary.json'), 'w') as _summary:
    json.dump(dict_size, _summary)