'''
4. Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого
типа оргтехники.
'''


class Warehouse:
    def __init__(self, bld, floor, sector):
        self.bld = bld
        self.floor = floor
        self.sector = sector


class Office_Tech:
    def __init__(self, brand, model, weight, price):
        self.brand = brand
        self.model = model
        self.weight = weight
        self.price = price


class Printer(Office_Tech):
    def __init__(self, brand, model, weight, price, print_speed):
        Office_Tech.__init__(self, brand, model, weight, price)
        self.print_speed = print_speed


class Scanner(Office_Tech):
    def __init__(self, brand, model, weight, price, scan_speed):
        Office_Tech.__init__(self, brand, model, weight, price)
        self.scan_speed = scan_speed


class Multifunc_Dev(Office_Tech):
    def __init__(self, brand, model, weight, price, scan_speed, print_speed):
        Office_Tech.__init__(self, brand, model, weight, price)
        self.scan_speed = scan_speed
        self.print_speed = print_speed


device = Printer('Epson', 'd240', 7, 380, 60)
print(device.brand)

