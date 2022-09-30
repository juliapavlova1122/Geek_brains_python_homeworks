


import random
import copy

# n = int(input('Введите количество элементов '))
# input_list = [i for i in range(n)]
# # result_list = copy.deepcopy(input_list) # глубокая копия для сложных списков

# result_list = input_list[:]
# # random_shuffle(result_list)

# for i in range(n):
#     index_random = random.radient(0, n - 1)
#     result_list[i], result_list[index_random] = result_list[index_random], result_list[i]

# print('', input_list)
# print('', result_list)


# # import random
# # a = [1, 2, 3, 4, 10, 11, 23, 56]
# # random.shuffle(a, random.random)
# # print(a)


from copy import copy


my_list = [1,2], [3,4] # внутри списка вложенный список
# my_list2 = my_list[:]
my_list2 = copy.deepcopy(my_list)
my_list[0].append(7)
print(my_list2)


# # Реализуйте алгоритм перемешивания списка.
# import random 
# import copy

# # n = int(input("Введите количество элементов: "))
# # input_list = [i for i in range(n)]
# # result_list = copy.deepcopy(input_list)
# # #result_list = input_list[:]
# # random.shuffle(result_list)
# # # for i in range(n):
# # #     index_random = random.randint(0, n - 1)
# # #     result_list[i], result_list[index_random] = result_list[index_random], result_list[i]
# #     # temp = result_list[i]
# #     # result_list[i] = result_list[index_random]
# #     # result_list[index_random] = temp
# # print("Исходный список",input_list)
# # print("Перемешанный список",result_list)

# my_list = [[1, 2], [3, 4]] # вложенный список
# #my_list2 = my_list[:]
# my_list2 = copy.deepcopy(my_list)
# my_list[0].append(5)
# print(my_list2)
