'''
1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей
структурой папок:

|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp

Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске
(как быть?); как лучше хранить конфигурацию этого стартера, чтобы в будущем
можно было менять имена папок под конкретный проект; можно ли будет при этом
расширять конфигурацию и хранить данные о вложенных папках и файлах
(добавлять детали)?

2. *(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта
со следующей структурой:

|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html

Примечание: структуру файла config.yaml придумайте сами, его можно создать
в любом текстовом редакторе «руками» (не программно); предусмотреть возможные
исключительные ситуации, библиотеки использовать нельзя.
'''

# возвращает список: [уровень в дереве, имя, является ли директорией]
def get_path_level(line):
    path_level = [None, None, None]
    line_split = line.split('|--')
    path_level[0] = int(len(line_split[0])/3)
    path_level[1] = line_split[1].strip('\n')
    path_level[2] = '.' not in path_level[1]
    return path_level

def create(line, pre_level, link):
    obj = get_path_level(line)
    if obj[2] == False:
        open(os.path.join(link, obj[1]), 'w').close()
        pre_level = obj[0]
        return pre_level, link
    if pre_level > obj[0]:
        link = os.path.join(link, '../' * (pre_level - obj[0]))
        os.chdir(link)

    os.chdir(link)
    os.mkdir(obj[1])

    pre_level = obj[0]
    link = os.path.join(link, obj[1])

    return pre_level, link

import os

yaml_link = 'config.yaml'
link = os.getcwd()
pre_level = 0
with open(yaml_link, 'r', encoding='utf-8') as yaml:
    for line in yaml:
        if line[0] == '#' or line.strip('\n') == '':
            pass
        else:
            pre_level, link = create(line, pre_level, link)


