# Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.



# со словарем
# dict_new = {}

# items = numpy.random.radint(10, size = 10)
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


# ------------------
import numpy
from collections import Counter

items = numpy.random.radint(10, size = 10)
items_set = list(items[:10])
print(*items_set)

dict_new = Counter(items_set)

res_list = [i for i in dict_new if dict_new[i] == 1]

print(*res_list)




#----------------
from collections import Counter
from random import randint

def create_list(k, m, n):    # создание списка случайных чисел указанного диапазона в соответствии с указанным количеством элементов
    return [randint(m, n) for i in range(k)]


k = int(input("Введите количество чисел в списке: "))
m = int(input("Введите нижнюю границу чисел: "))
n = int(input("Введите верхнюю границу чисел: "))
input_list = create_list(k, m, n)
output_list = [k for k, v in Counter(input_list).items() if v == 1]
print("Исходная последовательность чисел: ", input_list)
print("Неповторяющиеся числа: ", output_list)


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

#=========================

from collections import Counter


items = numpy.random.randint(10, size=10)
items_set = list(items[:10])
print(*items_set)

dict_new = Counter(items_set)
res_list = [i for i in dict_new if dict_new[i] == 1]

print(*res_list)

# for i in items_set:
#     if not i in dict_new:
#         dict_new[i] = 0
#     dict_new[i] += 1

# res_list = []
# for i in dict_new:
#     if dict_new[i] == 1:
#         res_list.append(i)
# print(*res_list)

#=========================

from collections import Counter


items = numpy.random.randint(10, size=10)
items_set = list(items[:10])
print(*items_set)

dict_new = Counter(items_set)
res_list = [i for i in dict_new if dict_new[i] =
dict_new = Counter(items_set)
res_list = [i for i in dict_new if dict_new[i] == 1]

print(*res_list)

