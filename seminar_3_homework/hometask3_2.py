# 2 Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list1 = [2, 3, 4, 5, 6]
result_list = []

for i in range (1, len(list1) - 1):
    multiplication = list1[i-1] * list1[-i]
    result_list.append(float(multiplication))
    
print(f'Произведение пар чисел списка: ', result_list)






