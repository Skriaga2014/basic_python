'''
5. Реализовать класс Stationery (канцелярская принадлежность).

   определить в нём атрибут title (название) и метод draw (отрисовка).
   Метод выводит сообщение «Запуск отрисовки»;
   создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
   в каждом классе реализовать переопределение метода draw.
   Для каждого класса метод должен выводить уникальное сообщение;
   создать экземпляры классов и проверить, что выведет описанный метод
   для каждого экземпляра.
'''


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('message number 1')


class Pencil(Stationery):
    def draw(self):
        print('message number 2')


class Handle(Stationery):
    def draw(self):
        print('message number 3')


var0 = Stationery('000')
var0.draw()
var1 = Pen('001')
var1.draw()
var2 = Pencil('002')
var2.draw()
var3 = Handle('003')
var3.draw()


