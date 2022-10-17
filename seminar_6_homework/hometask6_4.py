# 3.3. Задайте список из вещественных чисел. Напишите программу, которая 
# найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


input_list = list(map(lambda x: float(x), input("Введите список чисел, разделенных пробелом: ").split()))
fract_lst = [round(i % 1, 3) for i in input_list]
dif = max(fract_lst) - min(fract_lst)
print(f"Разница между максимальным и минимальным значением дробной части элементов: {dif}")

exit()
# прошлое решение
input_list = [1.1, 1.2, 3.1, 5, 10.01]
# input_list = input("Введите список чисел, разделенных пробелом: ").split()

dif_list = []
i_max = 0 
i_min = 0
for i in range(len(input_list)):
    if float(input_list[i]) % 1 != 0:
        j = round((float(input_list[i]) % 1), 2)
        dif_list.append(j)
for i in range(len(dif_list)):
    if dif_list[i] > dif_list[i_max]: 
        i_max = i
    if dif_list[i] < dif_list[i_min]: 
        i_min = i
result = float(dif_list[i_max]) - float(dif_list[i_min])
print(f'Список исходный значений: ', input_list)
#print("Список дробных частей исходный значений:\n",fract_list)
print(f'Разница между максимальным и минимальным значением дробной части элементов: ', result)

