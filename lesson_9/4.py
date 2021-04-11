'''
4. Реализуйте базовый класс Car.

у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ
к атрибутам, выведите результат. Вызовите методы и покажите результат.
'''

# если машина не в движении, ее скорость 0, и она не может поворачивать


class Car:

    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.status = 'машина еще не начинала движение'

    def go(self):
        self.status = f'машина в движении со скоростью {self.speed} км/ч'
        return self.status

    def stop(self):
        if not self._is_motion():
            return 'машина и так стоит на месте'
        self.status = 'машина остановилась'
        return self.status

    def turn(self, side):
        if self.show_speed() == 0:
            return 'машина не может повернуть, так как стоит на месте'
        if side in ['право', 'лево']:
            side = 'на' + side
        self.status = f'машина повернула {side}'
        return self.status

    def show_speed(self):
        if not self._is_motion():
            return 0
        return self.speed

    def _is_motion(self):
        if self.status in ['машина еще не начинала движение',
                           'машина остановилась']:
            return False
        return True


class TownCar(Car):

    def show_speed(self):
        if not self._is_motion():
            return 0
        elif self.speed > 60:
            return 'превышение скорости'
        return self.speed


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if not self._is_motion():
            return 0
        elif self.speed > 40:
            return 'превышение скорости'
        return self.speed


class PoliceCar(Car):
    pass


car1 = TownCar(50, 'red', 'Lada', False)
car1.speed = 70

print(car1.stop())
print(car1.go())
print(car1.show_speed())
print(car1.stop())
print(car1.show_speed())
print(car1.turn('лево'))
print(car1.go())
car1.turn('лево')
print(car1.status)
