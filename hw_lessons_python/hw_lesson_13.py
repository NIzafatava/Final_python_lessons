

# 1. Написать бесконечный итератор, который возвращает случайно число в заданном диапазоне.
# Реализовать через класс-итератор и через функцию-генератор.
# Протестировать обе реализации в цикле for.

# Дополнительно (если есть время) добавить параметр стоп-число: как только генератор
# выдает стоп-число, он заканчивает генерировать новые.


# Через класс-итератор

import random

class Iterator:
    def __init__(self, start_num: int, last_num: int, stop_number: int = None):
        self.start_num = start_num
        self.last_num = last_num
        self.stop_number = stop_number

    def __next__(self):
        result = random.randint(self.start_num, self.last_num)
        if result == self.stop_number:
            raise StopIteration
        return result

    def __iter__(self):
        return self


my_iterator = Iterator(3, 9, 9)
for num in my_iterator:
    print(num)


#############
# через функцию-генератор


def generator(start_num: int, end_num: int, stop_number: int = None):
    while True:
        result = random.randint(start_num, end_num)
        if end_num == stop_number:
            break
        yield result


my_generator = generator(7, 15, 14)
for num in my_generator:
    print(num)

