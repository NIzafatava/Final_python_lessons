# 1
# Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# # Листва зеленела
# #
# # Требуется реализовать функцию longest_words(file),
# # которая выводит слово, имеющее максимальную длину.
#
#
# text = '''Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела'''
#
# with open('article.txt', 'w') as file:
#     file.write(text)
#
# def read(file_name: str) -> str:
#     with open('article.txt', 'r') as file:
#             words = file.read().split()
#             max_word = words[0]
#             for word in words[1:]:
#                 if len(max_word) < len(word):
#                     max_word = word
#             return max_word
#
#
# print(read('article.txt'))

# 2
# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file
# и выводить на печать построчно последние строки в количестве lines
# (на всякий случай проверим, что задано положительное целое число).
# Протестируем функцию на файле «article.txt» со следующим содержимым:
#
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

# def read_last(lines_number: int, file_name: str) -> None:
#     if lines_number < 0:
#         print('неверный параметр')
#         return
#     file = open(file_name)
#     lines = file.readlines()
#     for line in lines[-lines_number:]:
#         print(line)
#
#
#     file.close()
#
# read_last(-2, 'file1')




















