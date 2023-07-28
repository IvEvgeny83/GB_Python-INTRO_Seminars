# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел A . Последняя строка
# iсодержит число X

print('--------------START--------------')
import random
lenArray = int(input('Задайте требуемое количество элементов массива (от 1 до 10): '))
while lenArray < 1  or lenArray > 10:  # проверка корректности ввода данных
    print('Введена некорректная длина массива!')
    lenArray = int(input('Задайте требуемое количество элементов массива (от 1 до 10): '))
array = list()
for i in range(lenArray):   # наполняем массив указанной длины произвольными числами
    n = int(random.randint(0, 10))
    array.append(n)
numX = int(input('Введите число, которое необходимо найти в массиве (от 0 до 10): '))
while numX < 0 or numX > 10:    # проверка корректности ввода данных
    print('Введено некорректное значение поиска!')
    numX = int(input('Введите число, которое необходимо найти в массиве (от 0 до 10): '))
print(array)
max = array[0]
for i in range(len(array)):
    if array[i] == numX:
        print(f'\nЧисло {array[i]} массива {array} совпадает с заданным числом {numX} - исключаем его из результатов поиска.')
        i += 1
    else:
        if abs(array[i] - numX) < abs(max - numX):
            max = array[i]
print(f'\nЧисло {max} массива {array} является самым близким по величине к заданному числу {numX}.\n')


# #----------решение для автоматической проверки----------

# list_1 = [1, 2, 3, 4, 5]
# k = 6
# max = list_1[0]
# for i in range(len(list_1)):
#     if abs(list_1[i] - k) < abs(max - k):
#         max = list_1[i]
# print(max)