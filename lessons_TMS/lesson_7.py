# написать декоратор проверяющий что функция принимает целое число

from functools import wraps
from typing import Callable
#
#
#
#
# def validate_one_int_arg(func: Callable) -> Callable:
#     @wraps(func)
#     def inner(number: int) -> any:
#         if type(number) != int:
#             print('Ошибка')
#             return
#         return func(number)
#     return inner
#
#
# @validate_one_int_arg
# def is_even(number: int) -> bool:
#     return number % 2 == 0
#
#
# print(is_even(2))
# print(is_even('12'))


def cache(func: Callable) -> Callable:
    cached_data = {}
    @wraps(func)
    def inner(*args):
        # {(2, 3): 5, (3, 3): 6,....}
        if args in cached_data:
            return cached_data[args]
        result = func(*args)
        cached_data[args] = result
        return result
    return inner




@cache
def add(a, b):
    print('Выполняем тело ф-ции')
    return a + b

print(add(2, 3))
print(add(2, 5))
print(add(2, 3))




