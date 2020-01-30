# 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.

# def my_func(x, y):
#     if y == 0:
#         y = int(input('Введите число, отличное от нуля: '))
#         my_func(x, y)
#     else:
#         print(x / y)
#
# my_func(6, 0)

# 2. Реализовать функцию, принимающую несколько параметров, описывающих
# данные пользователя: имя, фамилия, год рождения, город проживания, email,
# телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

# def func_info(name='', surname='', birth_date='01.01.1900', city='', email='example@world.ru', phone=''):
#     print(name, surname, birth_date, city, email, phone)
#
# func_info(name = 'Ivan', surname= 'Ivanov', city='NY', phone='+79999999999')

# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
# возвращает сумму наибольших двух аргументов.
#
# def my_sum(x, y, z):
#     if ((x >= y) or (y >= x)) and ((x + y) > (x + z) or (y + z) < (x + y)):
#         print(x + y)
#     elif (y >= z) or (z >= y) and (y + z) > (x + z) or (y + x) < (y + z):
#         print(y + z)
#     else:
#         print(x + z)
#
# my_sum(2, 1, 2)

# 4. Программа принимает действительное положительное число x и целое отрицательное
# число y. Необходимо выполнить возведение числа x в степень y. Задание необходимо
# реализовать в виде функции my_func(x, y). При решении задания необходимо обойтись
# без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень
# с помощью оператора *. Второй — более сложная реализация без оператора *, предусматривающая
# использование цикла.
# С использованием ** все понятно, написал сразу без возведения в степень
# def my_funk(x, y):
#     if type(x) == int and x > 0:
#         if type(y) == int and y < 0:
#             for i in range(1, abs(y)):
#                 x *= x
#             print(1 / x)
#         else:
#             print('Введите корректные значения переменных!')
#             my_funk(x=int(input()), y=int(input()))
#     else:
#         print('Введите корректные значения переменных!')
#         my_funk(x=int(input()), y=int(input()))
# my_funk(3, -2)

# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить
# ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел
# будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный
# символ, выполнение программы завершается. Если специальный символ введен после нескольких
# чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
# x = 0
# def my_sum():
#     while True:
#         global x
#         my_list = input('Введите через пробел числа и я посчитаю их сумму: \n').split()
#         try:
#             new = [int(i) for i in my_list]
#             print(sum(new))
#             x += sum(new)
#             print('Общая сумма введенных чисел равна: ', x)
#         except:
#             my_list.pop()
#             new = [int(i) for i in my_list]
#             print(sum(new))
#             x += sum(new)
#             print('Общая сумма введенных чисел равна: ', x, '\n Программа завершена')
#             break
# my_sum()
# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и
# возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое
# слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

# def int_func(*args):
#     list = str(*args)
#     print(list.title())
#
# my_str = str(input('Введите строку, а я сделаю каждое слово с большой буквы: \n'))
# int_func(my_str)