# Создайте программу для игры в ""Крестики-нолики"".
# 3. Создайте программу для игры в "Крестики-нолики". Поле 3x3. Игрок - игрок, без бота.
print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)

board = list(range(1,10))

def draw_board(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)

def take_input(player_token):
   valid = False
   while not valid:
      player_answer = input("Куда поставим " + player_token+"? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_token
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)
main(board)

input("Нажмите Enter для выхода!")

exit()

#-----------------
def draw_board(b):   # игровое поле
    print("-" * 13)
    for i in range(3): 
        print("|", b[0 + i * 3], "|", b[1 + i * 3], "|", b[2 + i * 3])
        print("-" * 13)


def take_move(player_symbol):  # ход игрока с проверками
    valid = False
    while not valid:
        player_step = input("Куда поставим " + player_symbol + "? ")
        try:
            player_step = int(player_step)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число? ")
            continue
        if player_step >= 1 and player_step <= 9:
            if (str(board[player_step - 1]) not in "XO"):
                board[player_step - 1] = player_symbol
                valid = True
            else: 
                print("Эта клетка уже занята!")
        else: 
            print("Некорректный ввод. Введите число от 1 до 9")


def chek_win(b):   # проверка наличия победителя
    win_lines = [[0,1,2], # победные линии
                 [3,4,5],
                 [6,7,8],
                 [0,3,6],
                 [1,4,7],
                 [2,5,8],
                 [0,4,8],
                 [2,4,6]]
    win = ""
    for i in win_lines:
        if b[i[0]] == "X" and b[i[1]] == "X" and b[i[2]] == "X":
            win = "X"
        if b[i[0]] == "O" and b[i[1]] == "O" and b[i[2]] == "O":
            win = "O"         
    return win
 

def main_game(b):   # основная игра
    counter = 0   # победителя не будет раньше, чем на пятом ходу
    winner = False
    while not winner:
        draw_board(b)
        if counter % 2 == 0: 
            take_move("X")
        else: 
            take_move("O")
        counter += 1
        if counter > 4: # победителя не будет раньше, чем на пятом ходу
            tmp = chek_win(b)
            if tmp: 
                print("\n" + tmp, "выиграл!")
                winner = True
                break
            if counter == 9:
                print("Ничья!")
                break
    draw_board(b)


print("\nИгра Крестики-нолики для двух игроков ")
# Инициализация карты
board = [1,2,3,
         4,5,6,
         7,8,9]
 
main_game(board)
input("Нажмите Enter для выхода!")



