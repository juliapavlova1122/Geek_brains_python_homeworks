# Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.
# Сделала на примере последовательности из 20 чисел от 10 до 30.

import numpy
from collections import Counter

numbers = numpy.random.randint(10, 30, size = 20)
numbers_set = list(numbers[:20])
print(numbers_set)
dict_new = Counter(numbers_set)

res_list = [i for i in dict_new if dict_new[i] == 1]

print(f'Неповторяющиеся элементы последовательности: ', res_list)

# Вопрос: нашла в справке по Counter действие, которое по описанию должно выдавать 
# как раз неповторяющиеся элементы. но оно выдает все, сортируя от меньшего к большему. 
# Я не поняла описание или непривильно применяю метод?
# print(sorted(items_set)) # не работает
# >>> sorted(c)                       # list all unique elements
# ['a', 'b', 'c', 'd', 'e']

# #----------------
# Решения с семинара
# from collections import Counter
# from random import randint

# def create_list(k, m, n):    # создание списка случайных чисел указанного диапазона в соответствии с указанным количеством элементов
#     return [randint(m, n) for i in range(k)]


# k = int(input("Введите количество чисел в списке: "))
# m = int(input("Введите нижнюю границу чисел: "))
# n = int(input("Введите верхнюю границу чисел: "))
# input_list = create_list(k, m, n)
# output_list = [k for k, v in Counter(input_list).items() if v == 1]
# print("Исходная последовательность чисел: ", input_list)
# print("Неповторяющиеся числа: ", output_list)


# dict_new = {}

# items = numpy.random.randint(10, size=10)
# items_set = list(items[:10])
# print(*items_set)

# for i in items_set:
#     if not i in dict_new:
#         dict_new[i] = 0
#     dict_new[i] += 1

# res_list = []
# for i in dict_new:
#     if dict_new[i] == 1:
#         res_list.append(i)
# print(*res_list)


