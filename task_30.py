# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_elem = int(input('\nВведите первый элемент арифметической прогрессии: '))
diff_elem = int(input('Введите шаг арифметической прогрессии: '))
num_elem = int(input('Введите количество элементов арифметической прогрессии: '))

'''
---Решение №1---
'''

# array_arith_prog = list()
# for i in range(1, num_elem + 1):
#     array_arith_prog.append(first_elem + (i - 1) * diff_elem)

# print('Последовательность чисел заданной арифметической прогрессии:',*array_arith_prog)

'''
---Решение №2---
'''

arith_prog = [first_elem + (i - 1) * diff_elem for i in range(1, num_elem + 1)]

print('Последовательность чисел заданной арифметической прогрессии:',*arith_prog)