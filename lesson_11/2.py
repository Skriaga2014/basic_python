'''
2.
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой.
'''


class Excep_t(ZeroDivisionError):
    def __init__(self, txt):
        self.txt = txt

num1 = input('input num 1: ')
num2 = input('input num 2: ')

try:
    num1, num2 = int(num1), int(num2)
    if num2 == 0:
        raise Excep_t('деление на ноль')
    else:
        a = int(num1)/int(num2)
        print('result:', a)
except Excep_t as err:
    print(err)
except ValueError:
    print('введенное значение не является числом')

