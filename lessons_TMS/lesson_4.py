numbers = [1, 2, 5, 10]
# for i, number in enumerate(numbers):
#     #print(f'index={i}, value = {number}')
#     if i % 2 == 1:
#         print(number)

# for value in enumerate(numbers):
# #     if value[0] % 2 == 1:
# #         print(value[1])
#
# numbers = [5, 1, 2, 7, 4, 3, 8, 1, 10]
# # Заменить каждый второй элемент на 0
#
# for i, number in enumerate(numbers):
#     if i % 2 == 1:
#         numbers[i] = 0
# print(numbers)
#
# n = len(numbers)
# print(n)
# for i in range(n):
#     print(i)

# 3 способа итерации:
# - только по элементам : for num in numbers:
# - только по индексам: for index in range(len(numbers))
# - по индексам и по элементам : for index, number in enumerate(numbers)


# numbers = [5, 1, 2, 7, 4, 3, 8, 1, 10]

# for i, number in enumerate(numbers):
#     if number == 4:
#         continue
#     if i == 3:
#         continue
#     print(number)


# for i, number in enumerate(numbers):
#     if number == 4:
#         break
#     print(number)

# numbers = [5, 1, 2, 7, 4, 3, 8, 1, 10]
# index = 0
# while index < len(numbers):
#     print(numbers[index])
#     index +=1
# print('finished')

# numbers = [5, 1, 2, 7, 4, 3, 8, 1, 10]
# index = 0
# while True:


#     print(f'val = {numbers[index]}')
#     index +=1
#     print(f'index = {index}')
# print('finished')

# Дан список numbers = [5, 1, 2, 7, 4, 3, 8, 1, 10]
# Посчитать сумму элементов списка, не использую встроенную функцию sum

# numbers = [5, 1, 2, 7, 4, 3, 8, 1, 10]
# a = 0
# for number in numbers:
#     a += number
# print(a)
# print(sum(numbers))

# numbers = []
# a = 0
# for number in numbers:
#     a += number
# print(a)
# print(sum(numbers))

# Дан словарь:
# friends_phone_numbers = {
#     'Egor': 123,
#     'Liza': 555,
#     'Vanya': 908,
#     'Yana': 150,
# }
# Для каждого элемента словаря вывести на экран: "У друга <имя> номер телефона <номер>"

# friends_phone_numbers = {
#     'Egor': 123,
#     'Liza': 555,
#     'Vanya': 908,
#     'Yana': 150,
# }
#
# for name in friends_phone_numbers:
#     print(f'У друга {name} номер телефона {friends_phone_numbers[name]}')

# Пользователь вводит число. Проверить, если пользователь ввел какие-либо символы
# кроме цифр, вывести сообщение 'Вы ввели невалидное число", иначе вывести на экран сумму цифр числа.
# Сделать двумя способами (с циклом и без)

# number_str = input('Ввведите число: ')
# sum = 0
# if number_str.isdigit():
#     for symbol in number_str:
#         sum += int(symbol)
#     print(sum)
# else:
#     print('Вы ввели невалидное число')

# Пользователь вводит строку. Нужно посчитать сколько раз встречается каждый из символов строки
#
# string = input()
# set_ = set(string)
# for str in set_:
#     kol = 0
#     for str1 in string:
#         if str == str1:
#             kol+=1
#     print(kol)
#
# string = input()
# dict_ = dict()
# set_ = set(string)
#
#
# for str in string:
#     if str in dict_:
#         dict_[str]+= 1
#     else:
#         dict_[str]=1
# print(dict_)


dict_ = {'a': 1, 'b': 4}
print([dict_['b']])