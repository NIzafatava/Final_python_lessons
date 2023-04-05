

# 1. Написать бесконечный итератор, который возвращает случайно число в заданном диапазоне.
# Реализовать через класс-итератор и через функцию-генератор.
# Протестировать обе реализации в цикле for.

# Дополнительно (если есть время) добавить параметр стоп-число: как только генератор
# выдает стоп-число, он заканчивает генерировать новые.


# Через класс-итератор

import random

class Iterator:
    def __init__(self, start_num: int, last_num: int = None):
        self.start_num = start_num
        self.last_num = last_num

    def __next__(self):
        if self.last_num is not None and self.start_num > self.last_num:
            raise StopIteration
        result = random.randint(self.start_num, self.last_num)
        return result

    def __iter__(self):
        return self


my_iterator = Iterator(3, 100)
for num in my_iterator:
    print(num)
    if num == 9:
        break

# через функцию-генератор


def generator(start_num: int, end_num: int = None):
    while True:
        if end_num is not None and start_num >= end_num:
            break
        yield random.randint(start_num, end_num)


my_generator = generator(7, 15)
for num in my_generator:
    print(num)
    if num == 9:
        break
