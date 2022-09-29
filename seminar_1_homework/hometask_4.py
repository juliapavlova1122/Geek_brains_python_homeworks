# Напишите программу, которая по заданному номеру 
# четверти, показывает диапазон возможных координат 
# точек в этой четверти (x и y).

quarter_number = int(input('Введите номер четверти координат: '))

if quarter_number == 1:
    print('x ∈ (0, +∞); y ∈ (0, +∞)')

if quarter_number == 2:
    print('x ∈ (-∞, 0); y ∈ (0, +∞)')

if quarter_number == 3:
    print('x ∈ (-∞, 0); y ∈ (-∞, 0)')

if quarter_number == 4:
    print('x ∈ (0, +∞); y ∈ (-∞, 0)')

else:
    print('Запустите программу заново и введите номер четверти координат от 1 до 4')


# Не переводить из строки в int

# quarter_number = input('Введите номер четверти координат: ')

# if quarter_number == "1":
#     print('x ∈ (0, +∞); y ∈ (0, +∞)')
# elif quarter_number == "2":
#     print('x ∈ (-∞, 0); y ∈ (0, +∞)')
# elif quarter_number == "3":
#     print('x ∈ (-∞, 0); y ∈ (-∞, 0)')
# elif quarter_number == "4":
#     print('x ∈ (0, +∞); y ∈ (-∞, 0)')
# else:
#     print('Запустите программу заново и введите номер четверти координат от 1 до 4')
