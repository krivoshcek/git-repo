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
    def __init__(self, item, count):
        super().__init__(item, count)


    def __str__(self):
        return f'�������: {str(self.item)}, ����������: {str(self.item)}'

class Xerox(Equipment):
    def __init__(self, item, count):
        super().__init__(item, count)


    def __str__(self):
        return f'�������: {str(self.item)}, ����������: {str(self.item)}'

class Scaner(Equipment):
    def to_take(self, *scaner):
        for i in scaner:
            

    def __str__(self):
        return f'�������: {str(self.item)}, ����������: {str(self.count)}, �������������: {str(self.hd)}'

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



