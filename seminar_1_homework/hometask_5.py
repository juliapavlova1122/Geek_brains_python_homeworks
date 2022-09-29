# Напишите программу, которая принимает на вход 
# координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

#  d = √((хА – хВ)2 + (уА – уВ)2)

# x = int(input('Введите координаты точки 1: '))
# y = int(input('Введите координату y: '))

# from math import sqrt

print('Введите координаты точки 1:')
x1 = float(input('Координата X1 = '))
y1 = float(input('Координата Y1 = '))
print('Введите координаты точки 2:')
x2 = float(input('Координата X2 = '))
y2 = float(input('Координата Y2 = '))
print()
# dictance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (0.5)
import math
dictance = round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2),2)
print(f'Расстояние между точками с координатами: \n[x1 = {x1}, y1 = {y1}] и [x2 = {x2}, y2 = {y2}]')
print(f'составляет {dictance}')

# 5. Напишите программу, которая принимает на вход координаты двух точек и 
#    находит расстояние между ними в 2D пространстве. 
#    Пример:
#    A (3,6); B (2,1) -> 5,09
#    A (7,-5); B (1,-1) -> 7,21

# from math import sqrt

# ax = float(input('Enter the x coordinate of the point A: '))
# ay = float(input('Enter the y coordinate of the point A: '))

# bx = float(input('Enter the x coordinate of the point B: '))
# by = float(input('Enter the y coordinate of the point B: '))

# distance_2d = round(sqrt((bx - ax) ** 2 + (by - ay) ** 2), 2)
# print(distance_2d)

# #==========================

# ax = float(input('Enter the x coordinate of the point A: '))
# ay = float(input('Enter the y coordinate of the point A: '))

# bx = float(input('Enter the x coordinate of the point B: '))
# by = float(input('Enter the y coordinate of the point B: '))

# distance_2d = round(((bx - ax) ** 2 + (by - ay) ** 2) ** 0.5, 2)
# print(distance_2d)



