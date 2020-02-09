# Создать класс TrafficLight (светофор) и определить у него один атрибут color
# (цвет) и метод running (запуск). Атрибут реализовать как приватный. В рамках
# метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго
# (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение
# между режимами должно осуществляться только в указанном порядке (красный, желтый,
#                                                                  зеленый). Проверить
# работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
# соответствующее сообщение и завершать скрипт.
# import time
# class TrafficLight:
#     def __init__(self, color=None):
#         self._color = color
#         self.running()
#
#     def time_count(self, n):
#         self.n = n
#         for i in range(n):
#             print(f'Сейчас горит {self._color} Осталось {n} секунд')
#             n -= 1
#             time.sleep(1)
#
#     def running(self):
#         self._color = 'Красный'
#         self.time_count(7)
#         self._color = 'Желтый'
#         self.time_count(2)
#         self._color = 'Зеленый'
#         self.time_count(5)
#         self.running()
#
# trafficlight = TrafficLight()
# trafficlight.running()

# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина),
# width (ширина). Значения данных атрибутов должны передаваться при создании экземпляра
# класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого
# для покрытия всего дорожного полотна. Использовать формулу: длинаширинамасса асфальта для покрытия
# одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.
#
# class Road:
#     def __init__(self, lenght, width):
#         self.__lenght = lenght
#         self.__width = width
#         self.weight = 25
#         self.depth = 1
#
#     def formula(self):
#         return self.__lenght*self.__width*self.weight*self.depth
#
# a = Road(10, 20)
# print(a.formula())

# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен
# быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
# на базе класса Worker. В классе Position реализовать методы получения полного
# имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).
# staff = []
# class Worker:
#     def __init__(self, name, surname, position, **kwargs):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = kwargs
#         self.salary = self._income.get('zp') + self._income.get('bonus')
#         staff.append({'Имя': self.name, 'Фамилия': self.surname, 'Оклад': self.salary})
#
#
# class Position(Worker):
#     def get_full_name(self):
#         print(f'Сотрудник {self.surname} {self.name}')
#
#     def get_total_income(self):
#         print(self.salary)
# a = Position('Иван', 'Иванов', 'инженер', zp = 25, bonus = 10)
# b = Position('Семен', 'Пуговкин', 'бездельник', zp = 10, bonus = 5)
#
# for i in staff:
#     print('='*50)
#     for n in i:
#         print(f'{n}:{i[n]}')

# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).  А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите
# несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов
# TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Выполните вызов методов и также покажите результат.

# class Car:
#     def __init__(self, speed, color, name, is_police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = bool(is_police)
#         my_turn = ''
#
#     def go(self):
#         print(f'Твой автомобиль {self.name} едет со скоростью {self.speed} км/ч')
#         while True:
#             print(f'Текущая скорость равна {self.speed}')
#             up = input('Чтобы увеличить скорость на 10 км/ч введите "го"\n'
#                        'или введите любой знак для отмены: ')
#             if up.lower() == 'го':
#                 self.speed += 10
#             else:
#                 break
#         print(f'Едем со скоростью {self.speed} км/ч')
#
#     def stop(self):
#         self.speed = 0
#         print('Мы остановились')
#
#     def turn(self):
#         self.my_turn = input('Введите направление движения словами "вперед", "назад", "налево", "направо"\n'
#                      'Для выхода введите любую кракозябру:\n')
#         if self.my_turn == ("вперед" or "назад" or "налево" or "направо"):
#             print(f'Ваш автомобиль едет {self.my_turn}')
#             self.turn()
#         else:
#             print('Передали управление автопилоту')
#
#     def show_info(self):
#         print(f'Ваш {self.color} {self.name} едет со скоростью {self.speed} км/ч')
#
# class TownCar(Car):
#     def go(self):
#         print(f'Твой автомобиль {self.name} едет со скоростью {self.speed} км/ч')
#         while True:
#             print(f'Текущая скорость равна {self.speed}')
#             up = input('Чтобы увеличить скорость на 10 км/ч введите "го"\n'
#                        'или введите любой знак для отмены: ')
#             if up.lower() == 'го':
#                 self.speed += 10
#             else:
#                 break
#         if self.speed > 60:
#             a = input('Скорость слишком большая, можно получить штраф!\n'
#                       'Введите "да" чтобы снизить скорость до 60 или любой символ чтобы оставить как есть:\n')
#             if a == 'да':
#                 self.speed = 60
#         print(f'Едем со скоростью {self.speed} км/ч')
#
#
#     def show_info(self):
#         while self.speed > 60:
#             a = input('Скорость слишком большая, можно получить штраф!\n'
#                       'Введите "да" чтобы снизить скорость до 60 или любой символ чтобы оставить как есть:\n')
#             if a.lower() == 'да':
#                 self.speed = 60
#                 print(f'Ваш {self.color} {self.name} едет со скоростью {self.speed} км/ч')
#             else:
#                 print(f'Ваш {self.color} {self.name} едет со скоростью {self.speed} км/ч')
#                 break
#
# class WorkCar(Car):
#     def go(self):
#         print(f'Твой автомобиль {self.name} едет со скоростью {self.speed} км/ч')
#         while True:
#             print(f'Текущая скорость равна {self.speed}')
#             up = input('Чтобы увеличить скорость на 10 км/ч введите "го"\n'
#                        'или введите любой знак для отмены: ')
#             if up.lower() == 'го':
#                 self.speed += 10
#             else:
#                 break
#         if self.speed > 40:
#             a = input('Скорость слишком большая, можно получить штраф!\n'
#                       'Введите "да" чтобы снизить скорость до 60 или любой символ чтобы оставить как есть:\n')
#             if a == 'да':
#                 self.speed = 40
#     def show_info(self):
#         while self.speed > 40:
#             a = input('Скорость слишком большая, можно получить штраф!\n'
#                       'Введите "да" чтобы снизить скорость до 40 или любой символ чтобы оставить как есть:\n')
#             if a.lower() == 'да':
#                 self.speed = 40
#                 print(f'Ваш {self.color} {self.name} едет со скоростью {self.speed} км/ч')
#             else:
#                 print(f'Ваш {self.color} {self.name} едет со скоростью {self.speed} км/ч')
#                 break
#
# a = WorkCar(100, 'white', 'bmw', False)
# a.turn()

# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут
# title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из
# классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить
# уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
# import time
# class Stationery:
#     def __init__(self, title):
#         self.title = title
#
#     def draw(self):
#         print('Запуск отрисовки')
#         time.sleep(3)
#         print('Отрисовка завершена')
#
# class Pen(Stationery):
#     def draw(self):
#         print(f'Запуск отрисовки ручкой {self.title}')
#         time.sleep(3)
#         print('Отрисовка завершена')
#
# class Pencil(Stationery):
#     def draw(self):
#         print(f'Запуск отрисовки карандашом {self.title}')
#         time.sleep(3)
#         print('Отрисовка завершена')
#
# class Handle(Stationery):
#     def draw(self):
#         print(f'Запуск отрисовки маркером {self.title}')
#         time.sleep(3)
#         print('Отрисовка завершена')
# a = Pen('Parker')
# a.draw()
# b = Pencil('Kohinor')
# b.draw()
# c = Handle('Faber-Castel')
# c.draw()