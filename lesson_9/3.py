'''
3. Реализовать базовый класс Worker (работник).

    определить атрибуты: name, surname, position (должность), income (доход);
    последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
    элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
    создать класс Position (должность) на базе класса Worker;
    в классе Position реализовать методы получения полного имени сотрудника
    (get_full_name) и дохода с учётом премии (get_total_income);
    проверить работу примера на реальных данных: создать экземпляры
    класса Position, передать данные, проверить значения атрибутов,
    вызвать методы экземпляров.
'''

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

    # def write(self):
    #     print(self.name)
    #     print(self.surname)
    #     print(self.position)
    #     print(self._income)

class Position(Worker):

    def get_full_name(self):
        self.full_name = f'{self.name} {self.surname}'
        return self.full_name

    def get_total_income(self):
        self.total_income = self._income['wage'] + self._income['bonus']
        return self.total_income

worker1 = Position('ilia', 'salomatin', 'programmer', 10000, 2000)

print(worker1.name)
print('over methods:')
print('full name:', worker1.get_full_name())
print('total income:', worker1.get_total_income())
print('over attributes:')
print('full name:', worker1.full_name)
print('total income:', worker1.total_income)