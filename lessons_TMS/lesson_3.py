# print('g')

# print(bool(1))
# print(bool(0.0))
# print(bool(0.5))
# print(bool(int(0.5)))
# print(bool(255))
# print(bool(-256))

# print(bool('123'))
# print(bool(print))

# print(bool([1]))
# print(bool([]))

# num1 =1
# num2 = 2
# print(str(num1) + str(num2))

# list_ = list('abc')
# list_ = list({1, 2, 3})
# list_ = list(list_)
# print(list_)

# 8
# Есть массив чисел numbers = [5, 1, 2, 7, 4, 3, 8, 1, 10]. Нужно поменять местами первый и последний элементы.
# (двумя способами указать последний элемент).

# numbers = [5, 1, 2, 7, 4, 3, 8, 1, 10]
# # print(numbers[0])
# # print(numbers[-1])
# numbers[0], numbers[-1] = numbers[-1], numbers[0]

# tmp = numbers[0]
# numbers[0] = numbers[-1]
# numbers[-1] = tmp
# print(numbers)

# num = 1
# num += 2
# print(num)
#
# string = 'abc'
# string += 'd'
# print(string)
#
# list_ = [1, 2, 3]
# list_ += [5]
# print(list_)

# list_ = [1, 2, 3]
# list_ *= 2
# print(list_)

# list_ = ['c', 'a']
# # # print(sum(list_))
# # # print(max(list_))
# # # print(min(list_))
# # print(' '.join(list_))

# list_ = [1.3, 2.7]
# print(sum(list_))
# print(max(list_))
# print(min(list_))

# list_ = ['c', 'b', 'a']
# result = '-'.join(list_)
#
# template = 'My joint string is {}'
# print(f'My joint string is {result}')
# print(template.format(result))
# print(template.format('Hello'))

# num = 0
# result_str = str(num) if num else 'empty'

# if num:
#     result_str = str(num)
# else:
#     result = 'empty'
# print(result_str)

# 2 (на if else)
# Напишите программу, которая запрашивает у пользователя два числа (x и y) и выводит на экран результат их сравнения.
#
# Если x больше y, то программа должна вывести сообщение "x больше y".
# Если x меньше y, то программа должна вывести сообщение "x меньше y".
# Если x равно y, то программа должна вывести сообщение "x равно y".
# Однако, если x и y кратны 2, то программа должна вывести дополнительное сообщение "Оба числа кратны 2"

#
# x = int(input('Введите число x:'))
# y = int(input('Введите число y:'))
# if x > y:
#     print('x больше y')
# elif x < y:
#     print('x меньше y')
# elif x == y:
#     print('x равно y')
# if x % 2 == 0 and y % 2 == 0:
#     print('Оба числа кратны 2')

print(39 / 10)
print(39 // 10)
print(39 % 10)







