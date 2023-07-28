# Задача 2: Найдите сумму цифр трехзначного числа.

'''
Вариант решения №1
'''

print('---------------------------------')
number = input('Введите трёхзначное число: ')
while len(number) != 3:
    print ('Введённое число не является трёхзначным!')
    number = input('Введите трёхзначное число: ')
sum = 0
for i in range(len(number)):        #можно написать и range(3)
    n = int(number[i])
    sum = sum + n
print(f'Сумма чисел введённого трёхзначного числа {number} равна: {sum}')

'''
Вариант решения №2
'''

# print('---------------------------------')
# number = int(input('Введите число, сумму цифр которого хотите найти: '))
# sum = 0
# digNumber = number
# number_1 = number
# while digNumber > 0 :
#     number_1 = digNumber % 10
#     digNumber = digNumber // 10
#     sum = sum + number_1
# print(f'Сумма чисел введённого числа {number} равна: {sum}')