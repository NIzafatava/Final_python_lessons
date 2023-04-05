# https://www.w3resource.com/python-exercises/python-basic-exercises.php
# https://www.practicepython.org/


# 1. функция repr

# string = 'Hello'
# print(repr(string))

# result: 'Hello'

# 2. вывести дату через /

# exam_st_date = (11, 12, 2014)
# a, b, c = exam_st_date
# print(f'{a}/{b}/{c}')

# 3. узнать о функции

# print(sum.__doc__)

# 4. написать календарь

# import calendar
#
# y = int(input('Введите год : '))
# m = int(input('Введите месяц : '))
# print(calendar.month(y, m))

# 5. разница в днях между датами

# from datetime import date
# f_date = date(2014, 7, 2)
# l_date = date(2014, 7, 11)
# delta = l_date - f_date
# print(delta.days)

# 6. Concatenate all elements in a list into a string

# list_ = [1, 6, 8, 9]
# string_ = ''
# for i in list_:
#     string_ += str(i)
# print(string_)

# 7. Print out a set containing all the colors from a list which are not present in other list

# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
#
# not_in_2 = color_list_1.difference(color_list_2)
# not_in_1 = color_list_2.difference(color_list_1)
# print(not_in_2)
# print(not_in_1)

# 8. Write a Python program that computes the greatest common divisor (GCD) of two positive integers.

# def gcd(x, y):
#    gcd = 1
#    if x % y == 0:
#        return y
#    for k in range(int(y / 2), 0, -1):
#        if x % k == 0 and y % k == 0:
#            gcd = k
#            break
#    return gcd
# print("GCD of 12 & 17 =",gcd(12, 17))
# print("GCD of 4 & 6 =",gcd(4, 6))
# print("GCD of 336 & 360 =",gcd(336, 360))

# 9.  isinstance(isinstance(obj, classinfo) -> bool)Возвращает флаг, указывающий на то, является ли указанный объект экземпляром указанного класса (классов).

# a = 3
# print(isinstance(a, int))

# 10. Check if file exists

# import os.path
# print(os.path.isfile('lesson 4.py'))
#
# # 11. user
#
# import getpass
# print(getpass.getuser())
#
#
# 12. 32 bit or 64 bit

# import struct
# print(struct.calcsize("P") * 8)

# 13. словарь
#
# dict_ = {'Настя': 'Саша', 'Настя': 'Саша'}
# (a, b) = dict_.items()
# print(a)
# print(b)
# print(c)
# print(d)

# 14.Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
# also create a lambda function that multiplies argument x with argument y and prints the result.

# func1 = lambda x: x + 15
# func2 = lambda x, y: x * y
#
# print(func1(5))
# print(func2(5, 2))

# 15.  Write a Python program to create a function that takes one argument,
# and that argument will be multiplied with an unknown given number

# def mult(n):
#     return lambda x: x * n
#
# result = mult(3)
# print(result(2))

# 5. Write a Python program to filter a list of integers using Lambda. Go to the editor
# Original list of integers:
# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list_even = list(filter(lambda x: x % 2 == 0, list_))
# print(list_even)

# 6. Write a Python program to square and cube every number in a given list of integers using Lambda. Go to the editor
# Original list of integers:
# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list_1 = list(map(lambda x: x ** 2, list_))
# print(list_1)

# 7. Write a Python program to find if a given string starts with a given character using Lambda

# check_ = lambda x: True if x.startswith('к') else False
# print(check_('кат'))

# 8. Write a Python program to create Fibonacci series up to n using Lambda
# def det_fib(n):
#     if n == 1:
#         return 1
#     elif n == 0:
#         return 0
#     else:
#         return (det_fib(n-1) + det_fib(n -2))
#
# print(det_fib(int(4)))


# 9. Write a Python program to find palindromes in a given list of strings using Lambda. Go to the editor
# Orginal list of strings:

# list_ =  ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
# palindromes_ = list(filter(lambda word: word == word[::-1], list_))
# print(palindromes_)
#
# 10.  Write a Python program to find all anagrams of a string in a given list of strings using Lambda. Go to the editor
# Orginal list of strings:
#
# from collections import Counter
# list_ = ['bcda', 'abce', 'cbda', 'cbea', 'adcb']
# anagram_main = 'abcd'
# anagrams = list(filter(lambda word: Counter(word) == Counter(anagram_main), list_))
# print(anagrams)

# 11. Write a Python program to calculate the sum of the positive and negative numbers of a given list of
# numbers using the lambda function.

# list_ = [2, 4, -6, -9, 11, -12, 14, -5, 17]
# sum_positive = sum(list(filter(lambda x: x > 0, list_)))
# print(sum_positive)

# 12. Write a Python program to find a list with maximum and minimum length using lambda. Go to the editor
# Original list:

# list_ = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
#
#
# def max_length_list(input_list):
#     max_length = max(len(x) for x in input_list)
#     max_list = max(input_list, key=lambda i: len(i))
#     return (max_length, max_list)
#
# print(max_length_list(list_))


# 13.Sort each sublist of strings in a given list of lists using lambda

# list_ = [['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
#
#
# def sort_list(input_list):
#     result = [sorted(x, key = lambda x: x[0] ) for x in input_list]
#     return result
#
#
# print(sort_list(list_))

# 14. Write a Python program to sort a given list of lists by length and value using lambda. Go to the editor
# Original list:

# list_ = [[2], [0], [1, 3], [0, 7],  [13, 15, 17], [9, 11]]
#
# def sorted_list(input_list):
#     result = sorted(input_list, key= lambda l: (len(l), l))
#     return result
#
#
# print(sorted_list(list_))


# 15. Write a Python program to find the maximum value in a given heterogeneous list using lambda. Go to the editor
# Original list:

# list_ = ['Python', 3, 2, 4, 5, 'version']
# max_val = max(list_, key= lambda x: (isinstance(x, int), x))
# print(max_val)

# 16ю Write a Python program to remove None values from a given list using the lambda function. Go to the editor/
# Original list:
# list_ = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
#
# def remove_None(numbers):
#     new_list = list(filter(lambda num: num is not None, numbers))
#     return new_list
#
# print(remove_None((list_)))


# 17. Write a Python program to find the maximum and minimum values in a given list of tuples using the lambda function. Go to the editor
# Original list with tuples:

# list_ = [('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]
# max_value = max(list_, key= lambda x: x[1])[1]
# print(max_value)

# 18.  Write a Python program to count the occurrences of items in a given list using lambda. Go to the editor
# Original list:
#
# list_ = [3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
# def count_occurrences(nums):
#     result = dict(map(lambda el: (el, list(nums).count(el)), nums))
#     return result
#
# print(count_occurrences(list_))

# 19. Write a Python program to sort a given list of strings (numbers) numerically using lambda. Go to the editor
# Original list:
#
# list_ = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
# sorted_list = sorted(list_, key= lambda x: int(x))
# print(sorted_list)

# 20. Write a Python program to sort a given mixed list of integers and strings using lambda.
# Numbers must be sorted before strings. Go to the editor
# Original list:
# list_ = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
# def sorted_list(list1):
#     new_list = sorted(list1, key= lambda x: (isinstance(x, str), x))
#     return new_list
#
# print(sorted_list(list_))

# 21. Write a Python program to convert string elements to integers inside a given tuple using lambda. Go to the editor
# Original tuple values:
# list_ = (('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))
# new_list = tuple(map(lambda x: (int(x[0]), int(x[2])), list_))
# print(new_list)


# FUNCTIONS

# 1. Write a Python function to find the maximum of three numbers.
# def max_num(a, b, c):
#     result = max(a, b, c)
#     return result
#
# print(max_num(3, 1, 9))

# 2. Write a Python function to sum all the numbers in a list. Go to the editor
# list_ = (8, 2, 3, 0, 7)
#
# def sum_numbers(numbers):
#     sum = 0
#     for num in numbers:
#         num = int(num)
#         sum += num
#     print(sum)
#
# sum_numbers(list_)

# 3. Write a Python program to reverse a string. Go to the editor
#
# String = "1234abcd"
#
# def reverse_string(str_):
#     new_string = ''.join(reversed(str_))
#     print(new_string)
#
# reverse_string(String)

# 4.Write a Python function to calculate the factorial of a number (a non-negative integer).
# The function accepts the number as an argument.

# def fact(n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return 1
#     else:
#         return (fact(n- 1) * n)
#
# print(fact(5))

# 5.  Write a Python function to check whether a number falls within a given range.

# def num_in_range(num, n):
#     result = True if num in range(n) else False
#     return result
#
# print(num_in_range(150, 151))

# 6. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words
# in a hyphen-separated sequence after sorting them alphabetically. Go to the editor
# string_ = 'green-red-yellow-black-white'

# string_splited = string_.split('-')
# print(string_splited)
# string_splited_sorted = '-'.join(sorted(string_splited))
# print(string_splited_sorted)

# 7. Count the number of characters (character frequency) in a string

# def num_char(string):
#     dict = {}
#     for x in string:
#         keys = dict.keys()
#         if x in keys:
#             dict[x] += 1
#         else:
#             dict[x] = 1
#     return dict
#
# print(num_char('foof;'))

# 8. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$',
# except the first char itself. Go to the editor
# Sample String : 'restart'
#
# def change_char(str1):
#   char = str1[0]
#   str1 = str1.replace(char, '$')
#   str1 = char + str1[1:]
#
#   return str1
#
# print(change_char('restart'))


# 9. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.

# def change_string(string):
#
#     if len(string) >= 3 and string[-3:] != 'ing':
#         print(string + 'ing')
#     if len(string) >= 3 and string[-3:] == 'ing':
#         print(string + 'ly')
#     if len(string) < 3:
#         print(string)
#
# print(change_string('skying'))


# 10.  Write a Python script that takes input from the user and displays that input back in upper and lower cases.

# string = 'KFNK'
# print(string.lower())

# 11. Write a Python program that accepts a comma-separated sequence of words as input
# and prints the distinct words in sorted form (alphanumerically). Go to the editor
# words = 'red, white, black, red, green, black'
# words1 = ','.join(sorted(list(set(words.split(',')))))
# print(words1)
#
#
# 12. Write a Python program to insert space before every capital letter appears in a given word. Go to the editor
# Sample Data:
# ("PythonExercises") -> "Python Exercises"

# 13.List Overlap

# a = 'vbsbvfffv'
# b = 'vvoafh'
# a = set(a)
# b = set(b)
# c = list(set(a).intersection(set(b)))
# print(c)



