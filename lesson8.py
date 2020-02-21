""""
1. ����������� ����� �����, �������-����������� �������� ������ ��������� ���� � ���� ������
������� �����-�����-���. � ������ ������ ����������� ��� ������. ������, � ����������� @classmethod,
������ ��������� �����, �����, ��� � ��������������� �� ��� � ���� ������. ������, � �����������
 @staticmethod, ������ ��������� ��������� �����, ������ � ���� (��������, ����� � �� 1 �� 12). ���������
 ������ ���������� ��������� �� �������� ������.
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
#             print('��������� �������� �� ���������')
#
# Data.validation(Data.view('31', '02', '1990'))

""""
2. �������� ����������� �����-����������, �������������� �������� ������� �� ����. ��������� ��� 
������ �� ������, �������� �������������. ��� ����� ������������� ���� � �������� �������� ��������� 
������ ��������� ���������� ��� �������� � �� ����������� � �������.
"""
# class MyError(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
# a = input('����� ������ ����� 100 �� ��������� ����: ')
#
# try:
#     a = int(a)
#     if a == 0:
#         raise MyError("�� ���� ������ ������!")
#     else:
#         print(100 / a)
# except ValueError:
#     print('�� ����� �� �����')
#
# except MyError as err:
#     print(err)

"""
3. �������� ����������� �����-����������, ������� ������ ��������� ���������� ������ �� ������� ������ �����. 
��������� ������ ���������� �� �������� �������. ���������� ����������� � ������������ ������ � ��������� ������. 
�����-���������� ������ �������������� ���� ������ ��������� ������.
����������: ����� ������ �� �����������. �������� ������������� ����������, ���� ������������ ��� �� ��������� ������ 
�������, �����, ��������, ������� �stop�. ��� ���� ������ �����������, �������������� ������ ��������� �� �����.
"""
# class MyError(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
# my_list = []
# a = input('������� �����. ��� ���������� ������� "stop": ')
# while True:
#     try:
#         a = input()
#         if a == 'stop':
#             raise MyError('���� ����� �������')
#         else:
#             my_list.append(int(a))
#     except ValueError:
#         print('�� ����� �����, � �� �����!')
#     except MyError as err:
#         print(err, '\n��� ��������� ���� �����: \n', *my_list)
#         break
"""
4. ������� ������ ��� �������� ������ ����������. �������� �����, ����������� �����. � ����� ����� �����������, 
������� ����� ������� ��� �������-�����������. ��� ������ � ���������� ���� ���������� (�������, ������, �������). 
� ������� ������ ���������� ���������, ����� ��� ����������� �����. � �������-����������� ����������� ���������, 
���������� ��� ������� ���� ����������.
"""
class Equipment:
    def __init__(self, item, count):
        self.item = item
        self.count = count

    def __str__(self):
        print(self.item, self.count)

class Printer(Equipment):

    def __str__(self):
        return f'�������: {str(self.item)}, ����������: {str(self.item)}'

class Xerox(Equipment):

    def __str__(self):
        return f'�������: {str(self.item)}, ����������: {str(self.item)}'

class Scaner(Equipment):

    def __str__(self):
        return f'�������: {str(self.item)}, ����������: {str(self.item)}'

class Store:
    def __init__(self):
        self.printers = {}
        self.scaners = {}
        self.xeroxs = {}
        self.store = [self.printers, self.scaners, self.xeroxs]


    def get_printer(self, printer, count):
        try:
            if self.printers.get(printer) == None:
                self.printers.setdefault(printer.lower(), count)
            else:
                _ = self.printers.pop(printer) + count
                self.printers.setdefault(printer, _)
        except TypeError:
            print('�� ����� ������������ �������� ����������!')
        print(self.printers)

    def get_scaner(self, scaner, count):
        try:
            if self.scaners.get(scaner) == None:
                self.scaners.setdefault(scaner.lower(), count)
            else:
                _ = self.scaners.pop(scaner) + count
                self.scaners.setdefault(scaner, _)
        except TypeError:
            print('�� ����� ������������ �������� ����������!')

        print(self.scaners)

    def get_xerox(self, xerox, count):
        try:
            if self.xeroxs.get(xerox) == None:
                self.xeroxs.setdefault(xerox.lower(), count)
            else:
                _ = self.xeroxs.pop(xerox) + count
                self.xeroxs.setdefault(xerox, _)
        except TypeError:
            print('�� ����� ������������ �������� ����������!')

        print(self.xeroxs)

    def give_office(self, item, count):
        for i in self.store:
            try:
                a = i.pop(item) - count
                if a < 0:
                    print('�� ������ ������� ���!')
                    print(i)
                    break
                i.setdefault(item, a)
                print(f'�� �������� � ���� {item} � ���������� {count} ��')
                print(f'������� {item} �� ������: {a} ')
            except KeyError:
                pass
# ����� ���� ��������� � ��� ���������� �� ����� � ����� ������ get, �� ����� �� ��� ���� �������� � ����,
# ��� ��� ����� ������� ���.

b = Store()
b.get_xerox('canon', '20')
b.get_xerox('canon', 40)
b.get_printer('nikon', 20)
b.get_printer('nikon', 100)
b.get_printer('canon', 20)
print('=' * 20)
b.give_office('canon', 19)
