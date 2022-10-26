# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# Выигрышная стратегия- определить минимальную сумму двух ходов (в нашем случае 29),
# найти остаток от деления общего количества конфет / мир сумму 2 ходов 
# В нашем случае 2021 % 29 = 69*29 + 20
# Первый ход - 20 конфет, последующие ходы : 28 минус  ход второго игрока

# Игра с умным ботом (если умный бот ходит вторым - будет ловить человека на ошибке):

from random import randint

def Enter_date(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def printer(name, k, value):
    print(f"Ходил {name}, он взял {k}. Осталось на столе {value} конфет.")


def bot_step(value):
    k = value % 29
    if k == 0:
        k = randint(1,28)
    
    return k

player1 = input("Введите имя первого игрока: ")
player2 = "Bot"
value = 2021
flag = randint(0,1)
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0
counter2 = 0

while value > 28:
    if flag:
        k = Enter_date(player1)
        counter1 += k
        value -= k
        flag = False
        printer(player1, k, value)
    else:
        k = bot_step(value)
        counter2 += k
        value -= k
        flag = True
        printer(player2, k, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")

exit()

# Игра с обычным ботом без интеллекта:

from random import randint

def Enter_date(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def printer(name, k, value):
    print(f"Ходил {name}, он взял {k}. Осталось на столе {value} конфет.")


def bot_step(value):
    k = randint(1,28)

    return k

player1 = input("Введите имя первого игрока: ")
player2 = "Bot"
value = 2021
flag = randint(0,1)
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0
counter2 = 0

while value > 28:
    if flag:
        k = Enter_date(player1)
        counter1 += k
        value -= k
        flag = False
        printer(player1, k, value)
    else:
        k = bot_step(value)
        counter2 += k
        value -= k
        flag = True
        printer(player2, k, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")

exit()

# Игра человек против человека 
from random import randint

def Enter_date(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def printer(name, k, value):
    print(f"Ходил {name}, он взял {k}. Осталось на столе {value} конфет.")


def Enter_date2(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")

value = 2021
flag = randint(0,1)
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0
counter2 = 0

while value > 28:
    if flag:
        k = Enter_date(player1)
        counter1 += k
        value -= k
        flag = False
        printer(player1, k, value)
    else:
        k = Enter_date2(player2)
        counter2 += k
        value -= k
        flag = True
        printer(player2, k, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")

exit()
# # Решение с семинара
# import random
# from random import randint, choice


# def play_game0(a, b, pl, mes):   # игра человек против человека
#     count = choose_first_move()
#     print(f'\nПервый ход достаётся игроку {pl[count % 2]}')
#     while a > 0:
#         print(f'\n{pl[count % 2]}, {random.choice(mes)}')   # циклы перехода хода и попытки взять конфеты
#         move = int(input())
#         if move < 1 or move > b:
#             print(f'Не пытайтесь взять слишком много конфет, можно взять не более {b}, текущее количество конфет: {a}')
#             attempt = 3
#             while attempt > 0:
#                 if move <= a and move <= b and move > 0:
#                     break
#                 print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
#                 move = int(input())
#                 attempt -= 1
#             else: 
#                 return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
#         a -= move
#         if a > 0: 
#             print(f'Количество оставшихся конфет: {a}')
#         else: 
#             print('Все конфеты разобраны.')
#         count += 1
#     return pl[not count % 2]


# def play_game1(a, b, pl, mes):   # игра с ботом
#     count = choose_first_move()
#     print(f'\nПервый ход достаётся игроку {pl[count]}!')
#     while a > 0:
#         if count % 2:
#             move = randint(1, b)
#             print(f'\nБот-сластёна забрал {move}')
#         else:
#             print(f'\n{pl[0]}, {choice(mes)}')
#             move = int(input())
#             if move < 1 or move > b:
#                 print(f'Не пытайтесь взять слишком много конфет, можно взять не более {b}, текущее количество конфет: {a}')
#                 attempt = 3
#                 while attempt > 0:
#                     if move <= a and move <= b and move > 0:
#                         break
#                     print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
#                     move = int(input())
#                     attempt -= 1
#                 else:
#                     return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
#         a -= move
#         if a > 0:
#             print(f'Количество оставшихся конфет: {a}')
#         else:
#             print('Все конфеты разобраны.')
#         count += 1
#     return pl[count % 2]


# def play_game2(a, b, pl, mes):    # игра со смарт-ботом
#     count = choose_first_move()
#     print(f'\nПервый ход достаётся игроку {pl[count]}!')
#     while a > 0:
#         if count % 2:
#             move = a % (b + 1)
#             if move == 0:
#                 move = randint(1, b)
#             print(f'\nБот-сластёна забрал {move}')
#         else:
#             print(f'\n{pl[0]}, {choice(mes)}')
#             move = int(input())
#             if move < 1 or move > b:
#                 print(f'Не пытайтесь взять слишком много конфет, можно взять не более {b}, текущее количество конфет: {a}')
#                 attempt = 3
#                 while attempt > 0:
#                     if move <= a and move <= b and move > 0:
#                         break
#                     print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
#                     move = int(input())
#                     attempt -= 1
#                 else:
#                     return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
#         a -= move
#         if a > 0:
#             print(f'Количество оставшихся конфет: {a}')
#         else:
#             print('Все конфеты разобраны.')
#         count += 1
#     return pl[not count % 2]


# def choose_first_move():   #  определение игрока, делающего ход первым
#     return randint(0, 1)


# def introduce_players(d):
#     if d == 0:
#         player1 = input('\nДавайте познакомися. Первый игрок, как к Вам можно обращаться?\n')
#         player2 = input('\nВторой игрок, и Вы представьтесь, пожалуйста\n')
#         return [player1, player2]
#     else: 
#         player1 = input('\nДавайте познакомися. Как Вас зовут?\n')
#         player2 = 'Бот-сластёна'
#         print(f'\nЗа компьютер играет {player2}')
#         return [player1, player2]


# def game(d):
#     if d == 0: 
#         winner = play_game0(n, m, players, messages)
#     elif d == 1:
#         winner = play_game1(n, m, players, messages)
#     elif d == 2:
#         winner = play_game2(n, m, players, messages)

#     if not winner:
#         print('У нас нет победителя.')
#     else: print(f'Поздравляю! В этот раз победил {winner}! Ему достаются все конфеты!')

    
# greeting = ('\nЗдравствуйте! Это игра "Забери все конфеты!" '
#     '\nОсновные правила игры: '
#     '\nНам будет дано некоторое количество конфет, '
#     'за один ход мы можем взять не более определённого количества, '
#     'о котором мы с вами договоримся.'
#     '\nПраво первого хода будет определено случайным образом'
#     '\nИтак, начнём!\n')
            
# messages = ['Ваша очередь брать конфеты', 'возьмите конфеты', 
#             'сколько конфет возьмёте?', 'берите конфеты, не стесняйтесь', 'Ваш ход', 'берите конфетки', 'пора брать конфетки']

# print(greeting)

# n = int(input('Сколько конфет будем разыгрывать?\n'))
# m = int(input('Сколько максимально будем брать конфет за один ход?\n'))
# lvl = int(input('Выберите уровень сложности: '
#         '\n0 - Игра человек против человека'
#         '\n1 - Игра с компьютером'
#         '\n2 - Играс с компьютером, который любит конфеты\n'))

# players = introduce_players(lvl)
# winner = game(lvl)

# #-------------------------
# # from operator import or_
# # import os
# # import random

# # from sys import flags


# # def clear(): return os.system('cls')


# # clear()
# # print("Игра в конфеты (правила)\n")
# # print("На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.")
# # print("Первый ход определяется жеребьёвкой. ")
# # print("За один ход можно забрать не более чем 28 конфет. ")
# # print("Все конфеты оппонента достаются сделавшему последний ход. ")
# # print("Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?\n")
# # start = input("Нажминие Enter для продолжения\n")
# # # Цикл ввода имени первого игрока
# # clear()
# # candies = input(
# #     "Введите количество конфет с которым будете играть?\n\nНажминие Enter если не хотите вводить количеcтво\n")
# # if not candies:
# #     candies = 2021
# # else:
# #     candies = int(candies)
# # print(candies)
# # flags = True
# # clear()
# # while flags:
# #     name_player1 = input("Введите имя первого игрока: \n")
# #     clear()
# #     if not name_player1:
# #         print("Имя игрока не введено, прошу ввести имя первого игрока")
# #     else:
# #         flags = False
# # # Цикл ввода имени второго игрока
# # flags = True
# # clear()
# # while flags:
# #     name_player2 = input("Введите имя вторго игрока: \n")
# #     clear()
# #     if not name_player2:
# #         print("Имя игрока не введено, прошу ввести имя второго ")
# #     else:
# #         flags = False
# # clear()
# # # На данном моменте уже введы имена игроков.
# # flags_winners = True
# # flags = True
# # move = 0
# # quantity_candies_player1 = 0
# # quantity_candies_player2 = 0
# # while candies > 0:
# #     clear()
# #     move += 1
# #     flags = True
# #     while flags:
# #         part = 1
# #         print(f"Раунд {move} /({part})\n")
# #         print(f"Конфет у игрока {name_player1}, всего {quantity_candies_player1}")
# #         print(f"Конфет у игрока {name_player2}, всего {quantity_candies_player2}\n")
# #         print(f"Осталось конфет {candies}")
# #         try: 
# #             player1_candies = int(input(f"Игрок {name_player1} введите сколько хотите взять конфет от 1 до 28 \n"))
# #             clear() 
# #             if 1 <= player1_candies <= 28 and player1_candies <= candies:
# #                 candies -= player1_candies
# #                 quantity_candies_player1 += player1_candies
# #                 flags = False
# #             else:
# #                 print("Ошибка, введено некорректное количество конфет или ввели не число")         
# #         except ValueError:
# #                 print("Ошибка, введено некорректное количество конфет или ввели не число")         
# #     flags = True
# #     if candies == 0:
# #         flags = False
# #     while flags:
# #         part = 2
# #         print(f"Раунд {move} /({part})\n")
# #         print(f"Конфет у игрока {name_player1}, всего {quantity_candies_player1}")
# #         print(f"Конфет у игрока {name_player2}, всего {quantity_candies_player2}\n")
# #         print(f"Осталось конфет {candies}")
# #         try: 
# #             player2_candies = int(input(f"Игрок {name_player2} введите сколько хотите взять конфет от 1 до 28 \n"))
# #             clear() 
# #             if 1 <= player2_candies <= 28 and player2_candies <= candies:
# #                 candies -= player2_candies
# #                 quantity_candies_player2 += player2_candies
# #                 flags = False
# #             else:
# #                 print("Ошибка, введено некорректное количество конфет или ввели не число")         
# #         except ValueError:
# #                 print("Ошибка, введено некорректное количество конфет или ввели не число")             
# #         if candies == 0:
# #             flags_winners = False
# # clear()
# # if flags_winners == True:
# #     print(f"Выиграл игрок {name_player1}\n")
# #     print(f"Все конфеты переходят игроку {name_player1}")
# #     print(
# #         f"Конфеты всего конфеты игрока {name_player1}, всего  {player1_candies}")
# # else:
# #     print(f"Выиграл игрок {name_player2}")
# #     print(f"Все конфеты переходят игроку {name_player2}")
# #     print(
# #         f"Конфеты всего конфеты игрока {name_player2}, всего  {player2_candies}")

# # print(f"Сыгранно раундов за игру {move}\n")


