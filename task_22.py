# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

print('--------------START--------------\n')
import random
lenArray_1 = int(input('Задайте требуемое количество элементов массива №1 (от 1 до 10): '))
while lenArray_1 < 1 or lenArray_1 > 10:  # проверка корректности ввода данных
    print('Введена некорректная длина массива!')
    lenArray_1 = int(input('Задайте требуемое количество элементов массива №1 (от 1 до 10): '))
array_1 = [int(random.randint(0, 10)) for i in range(lenArray_1)] # наполняем массив указанной длины произвольными числами

lenArray_2 = int(input('Задайте требуемое количество элементов массива №2 (от 1 до 10): '))
while lenArray_2 < 1 or lenArray_2 > 10:  # проверка корректности ввода данных
    print('Введена некорректная длина массива!')
    lenArray_2 = int(input('Задайте требуемое количество элементов массива №2 (от 1 до 10): '))
array_2 = [int(random.randint(0, 10)) for i in range(lenArray_2)] # наполняем массив указанной длины произвольными числами

print('\nСформирован массив №1: ', *array_1)
print('Сформирован массив №2: ', *array_2)
array_1 = set(array_1)  #списоки переводим в множества
array_2 = set(array_2)
print('\nУпорядоченный набор чисел из сформированных массивов: ', *array_1.union(array_2))
print('\n---------------END---------------')