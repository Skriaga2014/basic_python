'''
1. Создать класс TrafficLight (светофор).

    определить у него один атрибут color (цвет) и метод running (запуск);
    атрибут реализовать как приватный;
    в рамках метода реализовать переключение светофора в режимы:
    красный, жёлтый, зелёный;
    продолжительность первого состояния (красный) составляет 7 секунд,
    второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
    переключение между режимами должно осуществляться только в указанном
    порядке (красный, жёлтый, зелёный);
    проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов.
При его нарушении выводить соответствующее сообщение и завершать скрипт.
'''

import time

class TrafficLight:

    def __init__(self, color, time):
        self.color = color
        self.time = time

    def running(self):
        for i in reversed(range(self.time)):
            print(f'{self.color}: {i + 1}')
            time.sleep(1)

red = TrafficLight('red', 7)
yellow = TrafficLight('yellow', 2)
green = TrafficLight('green', 5)
colors = [red, yellow, green, yellow]

while True:
    for color in colors:
        color.running()
