# 1.

check_odd_even = lambda x: 'even' if x % 2 == 0 else 'odd'
print(check_odd_even(int(input('Введите число: '))))

# 2.

list_ = [2, 7, 15, 23, 24, 64, 7, -1, -4]
result = list(map(lambda num: str(num), list_))
print(result)

# 3.

words = ('adda', 'fhwsk', 'kaasaak', 'jvgdln')
result = list(filter(lambda words: words == words[::-1], words))
print(result)

# 4.
# 4.1



from datetime import datetime
from difflib import SequenceMatcher

def decorator(func):
    def inner(text1, text2):
        time1 = datetime.now()
        result = func(text1, text2)
        time2 = datetime.now()
        total_time = time2 - time1
        print(f'Время выполнения: {total_time}')
        return result
    return inner


@decorator
def sequence_match(text1, text2):
    x = SequenceMatcher(None, text1, text2).ratio()
    print(x)


text1 = "My Name is Nastya"
text2 = "My Name is Nastya Izofatova"

print(sequence_match(text1, text2))


# 4.2

from datetime import datetime

def decorator(func):
    def inner(n):
        time1 = datetime.now()
        result = func(n)
        time2 = datetime.now()
        total_time = time2 - time1
        print(f'Время выполнения: {total_time}')
        return result
    return inner


@decorator
def findmissnum(n):
    numbers = set(n)
    leng = len(n)
    output = []
    for i in range(1, n[-1]):
        if i not in numbers:
            output.append(i)
    return output

list_ = [1, 2, 5]
print(findmissnum(list_))

# 5.


def check_string(string_: str) -> int|float:
        if string_.isdigit():
            string_int = int(string_)
            print(f'{string_int}, целое положительное число')
        else:
            for i in string_:
                if i[0] == '-' and '.' in string_:
                    print(f'{string_}, дробное отрицательное число')
                elif i[0] == '-':
                    string_int = int(string_)
                    print(f'{string_int}, целое отрицательное число')
                elif i[0] != '-' and '.' in string_:
                    print(f'{string_}, дробное положительное число')
                else:
                    for i in string_:
                        if i.isdigit == False and i[0] != 0 and (string_.count('.') > 1  or string_.count('.') == 1):
                            print(f'{string_}, Вы ввели некорретное число')

string_ = input('Введите строку (числа): ')
print(check_string(string_))




