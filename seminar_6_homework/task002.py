# Решение с семинара
# 
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# input_list = input("Введите список чисел, разделенных пробелом: ").split()
# prod_list = []
# if len(input_list) % 2 == 0: 
#     l = len(input_list) // 2   # для чётного числа эл-тов списка
# else: 
#     l = len(input_list) // 2 + 1                      # для нечётного числа эл-тов списка
# for i in range(l): 
#     prod_list.append(int(input_list[i]) * int(input_list[len(input_list) - 1 - i]))
# print("Исходный список",input_list)
# print("Результат перемножения пар чисел исходного списка",prod_list)


# Вариант написания кода выше с использованием Map и List Comprehension


def get_list_lenght(my_list): 
    if len(my_list) % 2 == 0: 
        le = len(my_list) // 2   # для чётного числа эл-тов списка
    else: 
        le = len(my_list) // 2 + 1                      # для нечётного числа эл-тов списка
    return le


input_list = list(map(int, input("Введите список чисел, разделенных пробелом: ").split()))
prod_list = [(input_list[i]) * (input_list[len(input_list) - 1 - i]) for i in range(get_list_lenght(input_list))]
print(input_list, prod_list)
