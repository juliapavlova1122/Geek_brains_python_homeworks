# 3.Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

# *Пример:*

# - Для n = 6: {1: 2, 2: 2.25, 3: 2.37, 4: 2.44, 5: 2.49, 6: 2.52}

n = int(input('Введите целое положительное число n '))
result_list = []
result_sum = 0
for i in range(1, n + 1):
    res_number = round(((1 + 1 / i) ** i), 3)
    result_list.append(float(res_number))
    result_sum += res_number
print('Сумма', n, 'чисел последовательности - ', result_sum)
print(result_list)



