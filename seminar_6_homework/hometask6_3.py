# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

natural_number = int(input("Введите число: "))
list1 = [i for i in range(1, natural_number) if natural_number % i == 0]

print(f"Простые множители числа {natural_number}: {list1}")

exit()
natural_number = int(input("Введите число: "))
i = 2 
list1 = []

while i <= natural_number:
    if natural_number % i == 0:
        list1.append(i)
        natural_number //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {natural_number}: {list1}")

