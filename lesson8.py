""""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором
 @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить
 работу полученной структуры на реальных данных.

"""
# import datetime
# class Data:
#     @classmethod
#     def view(cls, day, month, year):
#         return int(day), int(month), int(year)
#
#     @staticmethod
#     def validation(data):
#         day, month, year = data
#         try:
#             print(datetime.date(year, month, day))
#         except ValueError:
#             print('Введенное значение не корректно')
#
# Data.validation(Data.view('31', '02', '1990'))

""""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его 
работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа 
должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
# class MyError(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
# a = input('Будем делить число 100 на введенное вами: ')
#
# try:
#     a = int(a)
#     if a == 0:
#         raise MyError("На ноль делить нельзя!")
#     else:
#         print(100 / a)
# except ValueError:
#     print('Вы ввели не число')
#
# except MyError as err:
#     print(err)

"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список. 
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу 
скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
"""
# class MyError(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
# my_list = []
# a = input('Вводите числа. Для завершения введите "stop": ')
# while True:
#     try:
#         a = input()
#         if a == 'stop':
#             raise MyError('Ввод чисел окончен')
#         else:
#             my_list.append(int(a))
#     except ValueError:
#         print('Вы ввели букву, а не число!')
#     except MyError as err:
#         print(err, '\nВот введенные вами числа: \n', *my_list)
#         break
"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», 
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, 
уникальные для каждого типа оргтехники.
"""
class Equipment:
    def __init__(self, item, count):
        self.item = item
        self.count = count

    def __str__(self):
        print(self.item, self.count)

class Printer(Equipment):
    def __init__(self, item, count):
        super().__init__(item, count)


    def __str__(self):
        return f'Принтер: {str(self.item)}, количество: {str(self.item)}'

class Xerox(Equipment):
    def __init__(self, item, count):
        super().__init__(item, count)


    def __str__(self):
        return f'Ксерокс: {str(self.item)}, количество: {str(self.item)}'

class Scaner(Equipment):
    def to_take(self, *scaner):
        for i in scaner:
            

    def __str__(self):
        return f'Ксерокс: {str(self.item)}, количество: {str(self.count)}, автопереворот: {str(self.hd)}'

    # @property
    def give_to_store(self):
        return {(self.item, self.hd):self.count}

class Store:
    def __init__(self, printer=None, scaner=None, xerox=None):
        self.printer = {}
        self.scaner = {}
        self.xerox = {}


    def get_printer(self):

        for idx, item in a.give_to_store().items():
            for key, value in self.printer.items():
                if key == idx:
                    self.printer[value] += item
                else:
                    pass


        return self.printer


a = Scaner('12', 'sdf', True)
z = Scaner('13', 'sdf', True)
# a.give_to_store()
print(a.give_to_store())
# print(type(a.give_to_store()))
b = Store()

print(b.get_printer())


# b = Store
# print(b.get_printer)



