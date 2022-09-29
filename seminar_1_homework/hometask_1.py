# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day = int(input("Введите цифру, обозначающую день недели "))
if (1 <= day <= 5):
    print("Рабочий день")
# if (6 <= day <= 7):
if day == 6 or day == 7:
    print("Выходной")

if (day >= 8):
    print("Запустите программу заново и введите число от 1 до 7 ")


# num = int(input('Input the number of the day: '))

# while num < 1 or num > 7:
#     num = int(input('Wrong input. Try again here: '))
# else: 
#     if num == 6 or num == 7:
#         print('Yes')
#     else:
#         print('No')
