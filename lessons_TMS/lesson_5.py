# for, while

# string = 'abc' #False
# string = 'abcba' #True
#
# left_index = 0
# right_index = len(string) - 1
# while left_index != right_index:
#     if string[left_index] != string[right_index]:
#         print(False)
#         break
#     left_index += 1
#     right_index -= 1
# else:
#     print(True)



# def  add(a,b):
#     return a + b
#
#
# print(add(2, 3))
# print(add(a = 2, b = 3))
# # print(add(a = 2, b))
# print(add(2, b = 3))

# print(add())

# def add(a = 0, b = 0):
#     return a + b
#
#
# print(add())


# def get_list_with_1(a = []):
#     a.append(1)
#     return a
#
#
# print(get_list_with_1([3, 2]))
# print(get_list_with_1())
# print(get_list_with_1())

# def get_list_with_1(a = None):
#     if a is None:
#         a = []
#     a.append(1)
#     return a
#
#
# print(get_list_with_1([3, 2]))
# print(get_list_with_1())
# print(get_list_with_1())


# def get_average(*args):
#     return sum(args) / len(args)
#
#
# print(get_average(2, 3))
# print(get_average(2, 3, 4))
# list_ = [2, 3, 4]
# d = {10: 'a'}
# print(get_average(*list_))
# print(get_average(*d))
#
# def print_items(**kwargs):
#     for key in kwargs:
#         print(f'{key} is {kwargs[key]}')
#
#
# # print_items(name='Joe', surname = 'Wood', age=30)
# print_items()
#
#
# d = {
#     'name': 'Joe',
#     'age': 30,
# }
#
# print_items(**d)

# def foo(*args, **kwargs):
#     pass
#
#
# def add(a: int, b: int) -> int:
#     return a + b
#
#
# print(add(2, 3))
# print(add('a', 'b'))

# def get_sum(mubers: list[int]) -> int:
#     return sum(numbers)
#
#
# print(sum([1, 2, 3.5, 4, 5]))

# from typing import List, Dict, Optional, Set
#
#
# def get_sum(number: List[int], d: Optional[Dict[str, str]], s: Set[str]) -> int:
#     print(f'dict is {d}')
#     print(f'set is {s}')
#     return sum(numbers)


# #LEGB
# L - locale
# E -  enclosed
# G - global
# B - built-in


# Дан список чисел. Написать функцию, которая вернет сумму только положительных элементов списка

# numbers = [1, -2, 3, -4, 5]
# num2 = []
#
#
# def print_positive(numbers2: list[int]) -> int:
#     for num in numbers2:
#         if num > 0:
#             num2.append(num)
#
#
#     return sum(num2)
# print(print_positive(numbers))

# Дан список чисел. Написать функцию, которая вернет минимальное значение из списка.
# (Конкретно в этой задаче встроенную функцию min не использовать)
#
# def min_number(numbers: list[int]):
#     if numbers ==[]:
#         return None
#
#
#     min = numbers[0]
#     for num in numbers:
#         if num < min:
#             min = num
#     return min
#
#
# print(min_number([55, 88, 7, -10]))


# Написать функцию которая печатает числа от 0 до n, n - параметр.
# Если число делится на 3, вместо числа печатает fiWrite a Python program to create Fibonacci series up to n using Lambda
# Write a Python program to create Fibonacci series up to n using Lambda, если число делится на 5, вместо числа печатает buzz.
# Если число делится и на 3 и на 5, вместо числа печатает fizzbuzz


def pechat(n: int) -> None:
    for x in range(n):
        if x % 3 == 0 and x % 5 == 0:
            print('fizzbuzz', end=' ')
        elif x % 3 == 0:
            print('fizz', end=' ')
        elif x % 5 == 0:
            print('buzz',  end=' ')
        else:
            print(x, end=' ')

print(pechat(16))

