# 1
# Написать функцию, которая проверяет является ли целое число четным.
# Функция возвращает True, если число четное, False если нет.
# Если пользователь ввел не число, вывести ошибку, что введенные данные не являются числом.
# Ввод и вывод результата производится вне функции проверки



def check_even(number: int) -> None:
    if type(number) is not int:
        print('Введенные данные не является целым числом')
    elif type(number) is int and number % 2 == 0:
        print(True)
    else:
        print(False)

# # способ 1

print(check_even(16))
#
# # способ 2
number1 = 4
number2 = 9
number3 = 12.5
number4 = 'Hello'
print(check_even(number1))
print(check_even(number2))
print(check_even(number3))
print(check_even(number4))





# 2
# Написать функцию, которая принимает число n и выводит числа от 0 до n.
# Если число является четным, вывести квадрат числа, вместо числа.
# Для проверки на четность использовать функцию из задания 1.
# Если число делится на 7 и на 4 одновременно, процесс останавливается.
# Если пользователь ввел не число, вывести ошибку, что введенные данные не являются числом.

def pechat(n: int) -> None:
    if type(n) is not int:
        print('введенные данные не являются числом')
    else:
        for number in range(n):
            if number % 7 == 0 and number % 4 == 0:
                return
            elif check_even(number):
                print(number ** 2)
            else:
                print(number)

print(pechat(1))
