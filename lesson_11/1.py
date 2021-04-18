'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать
дату в виде строки формата «день-месяц-год». В рамках класса реализовать два
метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй, с декоратором
@staticmethod, должен проводить валидацию числа, месяца и года
(например, месяц — от 1 до 12). Проверить работу полученной структуры
на реальных данных.
'''

import datetime
import re

class Date:

    def __init__(self, date):
        self.date = date

    @classmethod
    def method1(cls, date):
        pattern = re.compile(r'((?P<day>\d+)\W(?P<month>\d+)\W(?P<year>\d+))')
        dt = pattern.search(date)

        return int(dt['day']), int(dt['month']), int(dt['year'])

    @staticmethod
    def method2(nums):
        nums = tuple(reversed(nums))
        try:
            result_date = datetime.date(*nums)
        except ValueError as error:
            quit(error)
        return result_date


d1 = Date('10-11-2021')
date_tuple = Date.method1(d1.date)
print(date_tuple)
date = Date.method2(date_tuple)
print(date)
