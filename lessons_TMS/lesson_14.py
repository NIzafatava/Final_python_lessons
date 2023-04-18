# 1. Реализовать генератор, который работает как enumerate. Для простоты работаем со списком



def gen_enum(list_: list):
    index = 0
    for item in list_:
        index += 1
        yield index, item

a = ['a', 'f', 's', 'l']
print(next(gen_enum(a)))
print(next(gen_enum(a)))


