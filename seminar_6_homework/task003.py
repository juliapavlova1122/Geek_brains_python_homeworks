# # Решение с семинара
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


# numb = input("Введите число: ") 
# sum1 = 0
# for digit in numb:
#     if digit.isdigit():
#         sum1 += int(digit)
# print(f"Сумма цифр числа {numb} равна:", sum1)


# Вариант с использованием List Comprehension

numb = input("Введите число: ") 
sum1 = sum([int(digit) for digit in numb if digit.isdigit()])
print(sum1)