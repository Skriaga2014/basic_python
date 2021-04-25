'''
6. Продолжить работу над вторым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад,
нельзя использовать строковый тип данных.
'''


class Storage:
    def __init__(self, base):
        self.base = {item: Storage_Line(**base[item]) for item in base}

    def moving(self, idx, qlt, move_to):
        if move_to == 'to_shop':
            self.base[idx].qlt_shop += qlt
            self.base[idx].qlt_storage -= qlt
        elif move_to == 'to_storage':
            self.base[idx].qlt_shop -= qlt
            self.base[idx].qlt_storage += qlt
        else:
            quit('error move_to')
        return self.base

    def move_device(self):
        try:
            idx = int(input('введите id перемещаемого товара: '))
            qlt = int(input('введите количество перемещаемого товара: '))
            to_dict = {1: 'to_shop', 2: 'to_storage'}
            to_ = int(input('перемещение (цифра): 1 - со склада в магазин, '
                            '2 - из магазина на склад: '))
            to_ = to_dict[to_]
        except ValueError:
            print('введенное значение не является числом, попробуйте снова')
            return 0
        try:
            self.moving(idx, qlt, to_)
        except KeyError:
            print(f'товара с индексом {idx} не существует, попробуйте снова')
            return 0
        print(f'товар с индексом {idx} в количестве {qlt} успешно перемещен')
        return 1

class Storage_Line:
    def __init__(self, qlt_storage, qlt_shop, obj):
        self.qlt_storage = qlt_storage
        self.qlt_shop = qlt_shop
        self.obj = obj

    def show_qlt(self):
        print('qlt storage:', self.qlt_storage)
        print('qlt shop:', self.qlt_shop)


class Office_Tech:

    def __init__(self, idx, brand, model, weight, price):
        self.id = idx
        self.brand = brand
        self.model = model
        self.weight = weight
        self.price = price
        print(f'new device: {brand} {model}')


class Printer(Office_Tech):
    def __init__(self, idx, brand, model, weight, price, print_speed):
        Office_Tech.__init__(self, idx, brand, model, weight, price)
        self.print_speed = print_speed

    def __str__(self):
        return f'Printer: {self.brand} {self.model}, ' \
               f'price ${self.price}, ' \
               f'print speed {self.print_speed} per minute, ' \
               f'width {self.weight}kg'


class Scanner(Office_Tech):
    def __init__(self, idx, brand, model, weight, price, scan_speed):
        Office_Tech.__init__(self, idx, brand, model, weight, price)
        self.scan_speed = scan_speed

    def __str__(self):
        return f'Scanner: {self.brand} {self.model}, ' \
               f'price ${self.price}, ' \
               f'scan speed {self.scan_speed} per minute, ' \
               f'width {self.weight}kg'


class Multifunc_Dev(Office_Tech):
    def __init__(self, idx, brand, model, weight, price, scan_speed,
                 print_speed):
        Office_Tech.__init__(self, idx, brand, model, weight, price)
        self.scan_speed = scan_speed
        self.print_speed = print_speed

    def __str__(self):
        return f'Multifunctional device: {self.brand} {self.model}, ' \
               f'price ${self.price}, ' \
               f'scan speed {self.scan_speed} per minute, ' \
               f'print speed {self.print_speed} per minute, ' \
               f'width {self.weight}kg'


base = {10056: {'qlt_storage': 86, 'qlt_shop': 2,
                'obj': Multifunc_Dev(10056, 'Epson', 'd240', 7, 380, 60, 70)},
        10057: {'qlt_storage': 99, 'qlt_shop': 8,
                'obj': Printer(10057, 'Canon', 'z540', 5, 150, 60)}}

storage1 = Storage(base)
# показывает характеристики товара по указанному id
print(storage1.base[10056].obj)
print('before moving:')
# показывает кол-во товара с указанным id на складе и в магазине
storage1.base[10056].show_qlt()
# перемещение товара (id товара, количество товара, куда перемещение)
storage1.moving(10056, 3, 'to_shop')
print('after moving:')
storage1.base[10056].show_qlt()
# добавление нового товара
scanner_epson_s580 = Scanner(10058, 'Epson', 's580', 6, 200, 80)
# добавление товара в базу склада с указанием количества на складе и магазине
storage1.base[10058] = Storage_Line(12, 3, scanner_epson_s580)
# вывод описания товара и его количества
print(storage1.base[10058].obj)
storage1.base[10058].show_qlt()

while not storage1.move_device():
    pass
