'''
3. Создать структуру файлов и папок, как написано в задании 2 (при помощи
скрипта или «руками» в проводнике). Написать скрипт, который собирает все
шаблоны в одну папку templates, например:

|--my_project
   ...
   |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html

Примечание: исходные файлы необходимо оставить; обратите внимание, что
html-файлы расположены в родительских папках (они играют роль пространств
имён); предусмотреть возможные исключительные ситуации; это реальная задача,
которая решена, например, во фреймворке django.
'''

import os
import shutil

my_proj_path = os.path.join(os.getcwd(), 'my_project')
tree = os.walk(my_proj_path)

for path in tree:
    path_split = path[0].rsplit('/', maxsplit=2)
    if path_split[-2] == 'templates':
        target_path = os.path.join(my_proj_path, 'templates', path_split[-1])
        shutil.copytree(path[0], target_path)
