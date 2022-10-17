# 3.2.Напишите программу, которая принимает на вход число N и выдает 
# набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from math import factorial

N = int(input('Введите число N: '))
f = lambda x: ((x == 1) and 1) or x * factorial(x -1)
list2 = list(f(i) for i in range(1, N +1))
print(list2)


exit()
N = int(input('Введите число N: '))
first_number = 1
res_list = []
for i in range(1, N + 1):
    first_number *= i
    res_list.append(int(first_number))
print(res_list)
# print(f'Набор произведений чисел от 1 до {N}:', res_list)