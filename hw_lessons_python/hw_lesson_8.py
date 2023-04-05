# 1
# -*- coding: utf-8 -*-
# str1, str2, str3, str4 = map(str, input('Введите 4 строки: ').split(' '))
# print(f'str1 = {str1}')
# print(f'str2 = {str2}')
# print(f'str3 = {str3}')
# print(f'str4 = {str4}')
#
# with open('file_hw_8.txt','w') as file:
#     file_data = file.write(str1)
#     file_data = file.write('\n')
#     file_data = file.write(str2)
#     file.close()
#
# with open('file_hw_8.txt','a') as file:
#     file_data = file.write('\n')
#     file_data = file.write(str3)
#     file_data = file.write('\n')
#     file_data = file.write(str4)
#     file.close()


# 2. file - 'file_hw_8.json'

# 3

import json
import csv

with open('file_hw_8.json') as json_file:
    json_data = json.load(json_file)
    print(json_data)


with open('file2_hw_8.csv', 'w') as csv_file:
    columns = ['id', 'name', 'age', 'telephon']
    writer = csv.writer(csv_file)
    writer.writerow(columns)
    for i in json_data:
        writer.writerow([i, json_data[i][0], json_data[i][1], ])
        writer.writerow([i,*json_data[i]], )
        # json_data[i] = value = ('name',12)






