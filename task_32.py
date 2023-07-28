# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random 

array = [int(random.randint(0, 10)) for i in range(random.randint(4, 10))]
min = int(input('\nВведите минимальное значение диапазона поиска элементов: '))
max = int(input('Введите максимальное значение диапазона поиска элементов: '))

'''
---Решение с применением функции---
'''

# def index_range(array, min, max):
#     index_list = []
#     for i in range(len(array)):
#         if min < array[i] < max:
#             index_list.append(i)
#     return index_list

# print('Сформированный произвольный массив: ', array)
# print('Индексы элементов массива, расположенных между значениями', min, 'и', max, ':', *index_range(array, min, max))

'''
---Простое решение---
'''

index_list = list()
print('Сформированный произвольный массив: ', array)

for i in range(len(array)):
    if array[i] > min and array[i] < max:
        index_list.append(i)

if len(index_list) != 0:
    print('Индексы элементов массива, расположенных между значениями', min, 'и', max, ':', *index_list)
else:
    print('Массив не содержит элементов, расположенных между значениями', min, 'и', max)