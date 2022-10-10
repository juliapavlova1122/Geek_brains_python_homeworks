# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

str_line = ''

file_1 = open('polynomial.txt', 'r')
file_2 = open('polynomial1.txt', 'r')

while True:
    line1 = file_1.readline()
    line2 = file_2.readline()
    if not line2 or not line1:
        break

    str_line = line1[:-5] + '+ ' + line2  # отрезаются до последних 4 символов, конкатенация (слияние)
 
    with open('polynomial_all.txt', 'w', encoding='utf-8') as file_my:
        file_my.write(f'{str_line}\n')
path = 'polynomial_all.txt' 
data = open(path, 'r') 
for line in data: 
    print(line) 

# Решение с семинара
# def get_coeffs(digits):
#     digits = digits.strip().strip(' = 0') # удаляет ' = 0'
#     digits = digits.split(' + ') # добавляет + в конец строки
#     coeffs = {}                 #  создает словарь
#     for i in digits:
#         a, *b = i.split(' * x ** ') 
#         if b:
#             coeffs[int(b[0])] = int(a)
#         else:
#             if i.endswith('x'):
#                 a, *b = i.split(' * x')
#                 coeffs[1] = int(a)
#             else:
#                 coeffs[0] = int(i)
#     return coeffs


# def sum_coeffs(d, coeffs):
#     for key in d:
#         if not key in coeffs:
#             coeffs[key] = 0
#         coeffs[key] += d[key]
#     return coeffs


# with open('res.txt') as f:
#     digits1 = f.read()
#     digits2 = digits1[:]
# coeffs1 = get_coeffs(digits1)
# coeffs2 = get_coeffs(digits2)
# coeffs = {}
# coeffs = sum_coeffs(coeffs1, coeffs)
# coeffs = sum_coeffs(coeffs2, coeffs)
# res = ''
# max_num = max(coeffs.keys())
# for i, j in coeffs.items():
#     res += str(j)
#     if i != 0 and j != 0 and i != 1:
#         res += ' * x ** '
#         res += str(i)
#         res += ' + '
#     elif j == 0:
#         continue
#     elif i == 1:
#         res += ' * x + '
#     else:
#         res += ' = 0'
# print(res)



#-------------
# Другое решение с семинара

# def poly_sum(name_1: str, name_2: str):
#     with open(name_1, "r", encoding="utf-8") as my_f_1, \
#             open(name_2, "r", encoding="utf-8") as my_f_2:
#         first = my_f_1.readlines()
#         second = my_f_2.readlines()

#         if len(first) == len(second):
#             with open("sum_poly.txt", "a", encoding="utf-8") as my_f_3:
#                 for i, v in enumerate(first):  # вернет кортеж от старта до конца строк
#                     my_f_3.write(f"{v[:-5]} + {second[i]}")
#         else:
#             print("The contents of the files do not match!")


# # poly_sum(input("Enter the file name 'text_1.txt': "), input("Enter the file name 'text_2.txt': "))
# poly_sum("poly.txt", "poly_2.txt")
