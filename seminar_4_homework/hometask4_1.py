# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import pi

import decimal
from decimal import Decimal

d = decimal.Decimal(input('Введите точность для числа в формате 0.001 ($10^{-1} ≤ d ≤10^{-10}$): '))
x = Decimal(d).as_tuple().exponent*(-1)

print (x)
print({round(pi, x)}) 

# ----------------------
# Решение с введением точности как целое яисло, оозначающее количество цифр после запятой
# from math import pi

# d = int(input('Введите целое число d, обозначающее точность числа: '))
# print({round(pi, d)})
