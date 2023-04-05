# Задание 1 (из презентации)

var_1 = (56, 'World', 256)
var_2 = (56, 'World', 256)
var_3 = (56, 'World', 256)
print(var_1 == var_2 == var_3)
print(id(var_1))
print(id(var_2))
print(id(var_3))

print('________________________________')

# Задание 2 (из презентации)

dict_1 = {'Katya': 'girl', 'Sergey': 'boy'}
dict_2 = {'Katya': 'girl', 'Sergey': 'boy'}
print(dict_1 == dict_2)
print(id(dict_1))
print(id(dict_2))
print(id(dict_1) is id(dict_2))

print('________________________________')

# Задание 3 (вывести из списка 2-ей и 4-е слово через запятую)

pets = ['cat', 'dog', 'fish', 'hamster', 'parrot']
a = pets[1]
b = pets[3]
print(f"{a}, {b}")

print('________________________________')
# Задание 4 (поменять местами с помощью распаковки кортежа)

a, b, c = (1, 2, 3)
a, b = b, a
print(a, b, c)
b, c = c, b
print(a, b, c)

print('________________________________')

# Задание 5 (словарь)

countries_capitals = {
    'Belarus': 'Minsk',
    'Poland': 'Warsaw',
    'Great Britain': 'London',
}
print(countries_capitals.get('Poland'))

print('________________________________')

# Задание 6 (список)

friends = ['Egor', 'Liza', 'Vanya', 'Yana']
name = input('Введите имя друга ')
if name in friends:
    print(f"У меня есть друг {name}")
else:
    print(f"У меня нет друга с именем {name}")












