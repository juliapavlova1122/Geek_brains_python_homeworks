# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# [Негафибоначчи]

n = int(input('Введите число: '))
def nega_fibo(n):
    list_nega_fibo = [0]
    if n == 0:
        return list_nega_fibo
    elif n == 1:
        list_nega_fibo = [1, 0, 1]
        return list_nega_fibo
    else:
        list_nega_fibo= [-1, 1, 0, 1, 1]
        fib1 = fib2 = 1
        for i in range(2, n):
            fib1, fib2 = fib2, fib1 + fib2  
            list_nega_fibo.append(fib2)
            list_nega_fibo.insert(0, (fib2 * (-1) ** i))
        return list_nega_fibo

print((f'Список чисел Негафибоначчи для {n}:{nega_fibo(n)}'))
    

# # рекурсия с лекции

# # Вариант 2

# def fibonacci(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)


# def nega_fibonacci(n):
#     list_negafibonacci = [0]
#     for i in range(1, n + 1):
#         list_negafibonacci.append(fibonacci(i))
#         list_negafibonacci.insert(0, (fibonacci(i) * (-1) ** (i + 1)))
#     return list_negafibonacci


# n = int(input("Введите число: "))
# print(f"Список чисел (нега)Фибоначчи для k = {n}: {nega_fibonacci(n)}")
