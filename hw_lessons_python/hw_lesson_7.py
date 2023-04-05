# Написать декоратор, который будет выводить в консоль
# имя функции, время вызова, и с какими параметрами она вызвана
# Примеры работы:
# add(1, 2) -> Функция add вызвана в 2023-03-14 22:21:53.986665 с позиционными параметрами (1, 2)
# add(a=1, b=2) -> Функция add вызвана в 2023-03-14 22:21:53.986703 с именнованными параметрами {'a': 1, 'b': 2}
# add(1, b=2) -> Функция add вызвана в 2023-03-14 22:21:53.986718 с позиционными параметрами (1,) и с именнованными параметрами {'b': 2}

# Дополнительно (если есть время) добавить код для обработки такого примера:
# add() -> Функция add вызвана в 2023-03-14 22:25:46.942232 без параметров


from functools import wraps
from typing import Callable
from datetime import datetime


def display_name_time_parameters(func: Callable) -> Callable:
    @wraps(func)
    def inner (*args, **kwargs):
        call_time = datetime.now()
        result = func(*args, **kwargs)
        func_name = func.__name__
        if not args and not kwargs:
            print(f'Функция {func_name} вызвана в {call_time} без параметров')
            # return
        elif kwargs == {}:
            print(f'Функция {func_name} вызвана в {call_time} с позиционными параметрами {args}')
            # return
        elif args == ():
            print(f'Функция {func_name} вызвана в {call_time} с именованными параметрами {kwargs}')
            # return
        else:
            print(f'Функция {func_name} вызвана в {call_time} с именованными параметрами {kwargs} и позиционными параметрами {args}')
        return result
    return inner


@display_name_time_parameters
def add(a, b):
    return

# print(add())
print(add(2, 3))
print(add(2,b= 3))








