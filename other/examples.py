# Встроенные модули

# from decimal import Decimal
# a = Decimal('0.9')
# b = Decimal('0.2')
# print(a+b == Decimal('1.1'))

# import time
# time.sleep(3)
# print('hello')

# import datetime as d, time, sys, os, platform
# time.sleep(3)
# print(d.datetime.now().time())
# print(sys.path)
# print(os.name)
# print(platform.system)

# import random
# print(random.random())

# from math import sqrt as s, ceil
# print(s(100))
# print(ceil(s(100)))
# print(round(s(100)))

# from math import ceil, floor
# a = 5.5
# b = 5.6
# c = 5.4
# d = 5.0
# print(round(a), round(b), round(c))
# print(ceil(a), ceil(b), ceil(c), ceil(d))
# print(floor(a), floor(b), floor(c), floor(d))

# list = [1, 3, 'Nastya']
# list[2]=4
# print(list)
# list.pop(0)
# print(list)

# string = "Follow you  dream! "
# print(string.lstrip())

# dict = {'Nastya': 'girl', 'Sasha': 'boy'}
# dict.update({'Natya': 'girl'})
# print(dict['Sasha'])
# print.pop('Natya')


# a, b, c = (1, 2, 3) с помощью распаковки кортежа меняются местами переменные
# a, b = b, a
# print(a, b, c)
# b, c = c, b
# print(a, b, c)

# pets = ['cat', 'dog', 'fish', 'hamster', 'parrot']
# a = pets[1]
# b = pets[3]
# print(f"{a}, {b}")

# var = None
# print(var is None)

# a = [1, 2, 3]
# b = [1, 2, 3]
# print(id(a))      #разные айди
# print(id(b))
# c = [3, 7, 0]
# a.append(c)
# print(a)
# print(id(a))    #append и extend не изменяет айди

# string = 'Hello Nastya'
# new_string= string.split('a')
# print(new_string)

# string = 'Sasha_Nastya'
# string1 = string.split('_')
# print(string1)
# string2 = ', '.join(string1)
# print(string2)

# *a, b, c = ['Sasha', 'Nastya', 'Lena', 'Liza']
# print(a)
# print(b)
# print(c)

# list_3 = list_2[:]    #копия с разными айди


# # 8
# # Есть массив чисел numbers = [5, 1, 2, 7, 4, 3, 8, 1, 10]. Нужно поменять местами первый и последний элементы.
# # (двумя способами указать последний элемент).
#
# numbers = [5, 1, 2, 7, 4, 3, 8, 1, 10]
# print(numbers.[0])
# print(numbers[-1])

# str1_sort = ['aabc']
# str2_sort = ['abbc']
# str1_sort_nodupl = "".join(set(str1_sort))
# str2_sort_nodupl = "".join(set(str2_sort))
# print(str1_sort_nodupl)
# print(str2_sort_nodupl)

# a = input('ВВ: ')
# a1 = " ".join(set(a))
# print(a1)

# 1
# Написать программу, которая получает имя и возраст пользователя, проверяет, что возраст 18 лет и старше
# и выдает приветсвенное сообщение в зависимости от возраста. Примеры работы:
# Имя Иван, возраст 34 -> "Приветсвую, Иван! У вас есть доступ к взрослому контенту."
# Имя Лиза, возраст 15 -> "Приветсвую, Лиза! У вас нет доступа к взрослому контенту."
# Имя Артем, возраст 18 -> "Приветсвую, Артем! Поздравляю с совершеннолетием! У вас есть доступ к взрослому контенту."

# name = input('Введите ваше имя:')
# age = int(input('Введите ваш возраст:'))
# if age > 18:
#     print(f'Приветствую, {name}! У вас есть доступ к взрослому контенту.')
# elif age == 18:
#     print(f'Приветствую, {name}! Поздравляю с совершеннолетием! У вас есть доступ к взрослому контенту.')
# else:
#     print(f'Приветствую, {name}! У вас нет доступа к взрослому контенту.')

# 2*
# Пользователь вводит две строки. Нужно вывести True, если в обеих строках использовались одинаковые символы,
# и False иначе. Постараться решить, не используя циклы.
# Примеры работы:
# "abc" и "bca" -> True
# "aabc" и "abc" -> True
# "Abc" и "abc" -> False
# "abc" и "aaa" -> False

#
# str1 = input('Введите значение строки 1: ')
# str2 = input('Введите значение строки 2: ')
# str1_sort = sorted(str1)
# str2_sort = sorted(str2)
# str1_sort_nodupl = "".join(set(str1_sort))
# str2_sort_nodupl = "".join(set(str2_sort))
# if str1_sort == str2_sort:
#     print('True (одинаковая длина и одинаковые символы)')
# elif str1_sort != str2_sort and len(str1_sort) == len(str2_sort):
#     print('False (одинаковая длина, но разные символы)')
# elif len(str1_sort) != len(str2_sort):
#     if str1_sort_nodupl == str2_sort_nodupl:
#         print('True (разная длина и одинаковые символы)')
#     else:
#         print('False (разная длина и разные символы)')

# old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
# new_list = old_list
#
# new_list[2][2] = 9
#
# print('Old List:', old_list)
# print('ID of Old List:', id(old_list))
#
# print('New List:', new_list)
# print('ID of New List:', id(new_list))


# string_ = input('Введите строку (слова разделены одним пробелом): ')
# string_splited = string_.split(' ')
# string_splited_list = []
# for word in string_splited:
#     words_revers = word[::-1]
#     string_splited_list.append(words_revers)
# new_string = ' '.join(string_splited_list)
# print(new_string)

# numbers = [5, 1, 2, 7, 4, 3, 8, 1, 10]
# # Посчитать сумму элементов списка, не использую встроенную функцию sum
#
# sum_ = 0
# for num in numbers:
#     sum_ += num
# print(sum_)

# friends_phone_numbers = {
#     'Egor': 123,
#     'Liza': 555,
#     'Vanya': 908,
#     'Yana': 150,
# }
# # Для каждого элемента словаря вывести на экран: "У друга <имя> номер телефона <номер>"
#
# for name in friends_phone_numbers:
#     print(f'у друга {name} номер телефона {friends_phone_numbers[name]}')

# Пользователь вводит строку. Нужно посчитать сколько раз встречается каждый из символов строки
# string = input()
# set_ = set(string)
# for str in set_:
#     kol = 0
#     for str1 in string:
#         if str == str1:
#             kol+=1
#     print(str, kol)

# string = input()
# dict_ = dict()
# for str in string:
#     if str in dict_:
#         dict_[str] += 1
#     else:
#         dict_[str] = 1
# print(dict_)

 # 4*
# Ввести строку (считаем, что в начале и в конце строки нет пробелов,
# все слова в строке разделены одним пробелом). Для введенной строки
# изменить порядок символов в каждом слове в предложении,
# сохраняя при этом пробелы и первоначальный порядок слов.

# Вариант 1 (выводит столбцом)
#
# string_ = input('Введите строку (слова разделены одним пробелом): ')
# string_splited = string_.split(' ')
# string_splited_list = []
# for word in string_splited:
#     words_revers = word[::-1]
#     string_splited_list.append(words_revers)
# new_string = ' '.join(string_splited_list)
# print(new_string)
#
# # Вариант 2 (выводит строкой)
#
# string_ = input('Введите строку (слова разделены одним пробелом): ')
# string_splited = string_.split(' ')
# words_revers = [word[::-1] for word in string_splited]
# new_string = ' '.join(words_revers)
# print(new_string)


 # def get_list_with_1(a=[]):
 #  a.append(1) # добавляем в список число 1
 #  return a
 # print(get_list_with_1([3, 2])) # [3, 2, 1], все ок
 # print(get_list_with_1()) # [1], все ок
 # print(get_list_with_1()) # [1, 1], неправильно, должно быть [1]

# def get_list_with_1(a=None):
#  if a is None:
#    a = []
#  a.append(1) # добавляем в список число 1
#  return a
# print(get_list_with_1([3, 2])) # [3, 2, 1], все ок
# print(get_list_with_1()) # [1], все ок
# print(get_list_with_1()) # [1, 1], неправильно, должно быть [1]


# def get_average(*args):
#  return sum(args) / len(args)

# print(get_average(1))

# print(check_is_positive2(0))

# 2. Написать функцию, которая принимает список чисел и выводит их в формате:
# <число>: <положительное/отрицательное>, одна запись на одной строке.
# Использовать для проверки функцию из первого задания.


# def print_numbers(numbers: list) -> None:
#     for number in numbers:
#         if number % 5 == 0:
#             return
#         result = "положительное" if check_is_positive(number) else "отрицательное"
#         print(f'{number}: {result}')

#
import random
#
# print(random.randint(-10, 10))
# n = 10
# list_ = []
# # for _ in range(n):
# #  list_.append(random.randint(-10, 10))
# # print(list_)
#
#
# list_ = [random.randint(-10, 10) for _ in range(n) ]
# print(list_)

# symbols = ['a', 'b', 'd']
# # print([random.choice(symbols) for _ in symbols])
# #
# dict_ = {s: random.randint(-10, 10) for s in symbols}
# print(dict_)

# # map, filter
# list_ = [-2, 4, 1, 12, -22]
# # print(list_)
# # positive_list = [item for item in list_ if item > 0]
# # print(positive_list)
#
# def is_positive(num: int) -> bool:
#     return num > 0
# positive_list2 = list(filter(is_positive, list_))
# print(positive_list2)

# # num1, num2 = map(int, [input('Первое число: '), input('Второе число: ')])
# # print(num1, num2, type(num1), type(num2))


z = '1.44'
z1 = '1..44'
print(z1.count('.'))