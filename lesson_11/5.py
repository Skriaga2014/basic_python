'''
5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают
за приём оргтехники на склад и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также
других данных, можно использовать любую подходящую структуру (например, словарь).
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


class Storage_Line:
    def __init__(self, qlt_storage, qlt_shop, obj):
        self.qlt_storage = qlt_storage
        self.qlt_shop = qlt_shop
        self.obj = obj

    @property
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
               f'scan speed {self.scan_speed} per minute,' \
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
print(storage1.base[10056].obj)
print('before moving:')
storage1.base[10056].show_qlt
storage1.moving(10056, 3, 'to_shop')
print('after moving:')
storage1.base[10056].show_qlt



