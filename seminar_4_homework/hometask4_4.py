# Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# Pn(x)=аnхn+an-1xn-1+аn-2хn-2+....+а2х2+a1х+а0,

from random import randint

def create_list(k, m, n):    # создание списка случайных чисел указанного диапазона в соответствии с указанной степенью уравнения
    return [randint(m, n) for i in range(k + 1)]

def create_polynomial(input_list):   # создание и форматирование многочлена на основании списка чисел
    polynomial_list = []
    for i in range(len(input_list)):
        if input_list[-1 - i] != 0:
            polynomial_list.insert(0, str(input_list[-1 -i]) + "*x^" + str(i)) 
    polynomial_str = " + ".join(polynomial_list)
    polynomial_str += " = 0"
    polynomial_str = polynomial_str.replace(" 1*", " ")
    polynomial_str = polynomial_str.replace("^1", "")
    polynomial_str = polynomial_str.replace("x^0", "1")
    polynomial_str = polynomial_str.replace("*1", "")
    if polynomial_str[0] == "1" and polynomial_str[1] == "*":
        n = 2 
        polynomial_str = polynomial_str[n:]  
    return polynomial_str
k = int(input("Введите степень уравнения: "))
m = int(input("Введите нижнюю границу чисел: "))
n = int(input("Введите верхнюю границу чисел: "))
input_list = create_list(k, m, n)
polynomial_list = create_polynomial(input_list)

print(input_list)
print(create_polynomial(input_list))

# with open('D:\\Обучение\\Практика\\Python\\Home_task4\\Polynomial_task004.txt', 'a') as data:
#     data.write(f"\n{create_polynomial(input_list)}")



