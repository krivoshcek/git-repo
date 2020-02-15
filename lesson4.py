Андрей Кривощек krivoshcek@gmail.com
# Реализовать скрипт, в котором должна быть предусмотрена функция расчета
# заработной платы сотрудника. В расчете необходимо использовать формулу:
# (выработка в часах*ставка в час) + премия. Для выполнения расчета для
# конкретных значений необходимо запускать скрипт с параметрами.
# from sys import argv
#
# script_name, count_hours, salary_hour = argv
#
# print("Имя скрипта: ", script_name)
# print("Введите количество отработанных часов: ", count_hours)
# print("Введите стоимость одного часа: ", salary_hour)
# print('Зарплата равна: ', int(count_hours) * int(salary_hour),
#        '\nПремия равна', (int(count_hours) * int(salary_hour)) * 0.3,
#        '\nИтого на руки вы получите: ', int(count_hours) * int(salary_hour) + (int(count_hours)*int(salary_hour)) * 0.3 )
#  2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
#
# import random
#
# list = [random.randint(1, 100) for el in range(1, 20)]
# new_list = [list[el] for el in range(len(list)) if list[el] > list[el - 1]]
# print('Исходный список: ', list, '\nРезультат: ', new_list)

#
# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.

# print([el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0])

# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести
# в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
# import random
# list = [random.randint(1, 10) for el in range(1, 15)]
# new_list = []
# print('Исходный ', list)
# for i in list:
#     if list.count(i) > 1:
#         pass
#     else:
#         new_list.append(i)
# print(new_list)

# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить
# результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

# from functools import reduce
# composition = reduce(lambda a, x: a * x, [el for el in range(100, 1001) if el % 2 == 0])
# print(composition)

# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

# from sys import argv
# import time
# import itertools
# script_name, count_start, count_stop = argv
#
# print("Имя скрипта: ", script_name)
# print("Введите начальное число: ", count_start)
# print("Введите число, до которого нужно считать: ", count_stop)
#
# for i in itertools.count(int(count_start)):
#     if i > int(count_stop):
#         break
#     else:
#         print(i)
#         time.sleep(1)
#
# from sys import argv
# import time
# import random
# from itertools import cycle
#
# script_name, count_stop = argv
# list = [random.randint(1, 10) for el in range(1, 5)]
# print("Введите количество повторений списка: ", count_stop)
# print('Исходный список: \n', list)
# check = 0
# for i in cycle(list):
#     if check >= int(count_stop) * len(list):
#         break
#     else:
#         print(i)
#     time.sleep(1)
#     check += 1
# Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение. При вызове функции должен создаваться
# объект-генератор. Функция должна вызываться следующим образом: for el
# in fact(n). Функция отвечает за получение факториала числа, а в цикле
# необходимо выводить только первые n чисел, начиная с 1! и до n!.
# n = int(input('Введите число факториала: '))
# result = 1
# def fact(n):
#     for i in range(1, n + 1):
#         yield i
# for i in fact(n):
#     print(i)
#     result *= i
# print(f'Факториал {n} равен: {result}')