from PIL import Image
import random

# global variables (only constants - no global keyword needed)
start = 1
end = 100

# function for rolling dice
def roll_dice():
    return random.randint(1, 6)

# function for showing board image
def show_board():
    img = Image.open("C:/Users/saisu/Downloads/SnakesAndLadderBoard.jpeg")
    img.show()

# if player gets ladder on their current position it shall allow them to climb the ladder and reach the updated position
def ladder(pos):
    if pos == 8:
        print('Ladder')
        return 26
    elif pos == 21:
        print('Ladder')
        return 82
    elif pos == 43:
        print('Ladder')
        return 77
    elif pos == 50:
        print('Ladder')
        return 91
    elif pos == 54:
        print('Ladder')
        return 93
    elif pos == 62:
        print('Ladder')
        return 96
    elif pos == 66:
        print('Ladder')
        return 87
    elif pos == 80:
        print("Ladder")
        return 100
    else:
        return pos
 
# if player steps on the snake position they shall go down to position where snake's tail is located
def snake(pos):
    if pos == 44:
        print('Snake')
        return 22
    elif pos == 46:
        print('Snake')
        return 5
    elif pos == 48:
        print('Snake')
        return 9
    elif pos == 52:
        print('Snake')
        return 11
    elif pos == 55:
        print('Snake')
        return 7
    elif pos == 59:
        print('Snake')
        return 17
    elif pos == 64:
        print('Snake')
        return 36
    elif pos == 69:
        print('Snake')
        return 33
    elif pos == 73:
        print('Snake')
        return 1
    elif pos == 83:
        print('Snake')
        return 19
    elif pos == 92:
        print('Snake')
        return 51
    elif pos == 95:
        print('Snake')
        return 24
    elif pos == 98:
        print('Snake')
        return 28
    else:
        return pos

# function for reaching at the end of game board
def reached_end(pos):
    if pos == end:
        return True
    else:
        return False
 
# function for player 1  (NO turn message here anymore)
def player_1(pos, player_name):
    # roll dice ONCE only
    dice = roll_dice()
    print("Dice rolled", dice)
    pos += dice
 
    # check if the current position is of snake or ladder
    pos = ladder(pos)
    pos = snake(pos)
 
    if pos > end:
        pos = end
 
    print(player_name, "your score is : ", pos)
    return pos

# function for player 2  (NO turn message here anymore)
def player_2(pos, player_name):
    # roll dice ONCE only
    dice = roll_dice()
    print("Dice rolled", dice)
    pos += dice
 
    # check if the current position is of snake or ladder
    pos = ladder(pos)
    pos = snake(pos)
 
    if pos > end:
        pos = end
 
    print(player_name, "your score is : ", pos)
    return pos
  
# main function for playing snakes and ladder game
def playgame():
    p1 = input("Player 1, Enter your name : ")
    p2 = input("Player 2, Enter your name : ")
 
    pos1 = start
    pos2 = start
    turn = 0
 
    while(True):
     
        if turn%2==0:
            print(p1, "it's your turn.")                    # ← added exactly like reference
            choice = input("1 : Go | 2 : Current Positions | 3 : Quit\n Enter your Choice : ")
            if choice == "3":
                print(p1," points :", pos1)
                print(p2," points :", pos2)
                print("Quitting the game, Thank you for playing !!!")
                break
            elif choice == "2":
                print(p1," points :", pos1)
                print(p2," points :", pos2)
                continue
            elif choice == "1":
                pos1 = player_1(pos1, p1)
                if reached_end(pos1):
                    print(p1,"won")
                    break
      
        else:
            print(p2, "it's your turn.")                    # ← added exactly like reference
            choice = input("1 : Go | 2 : Current Positions | 3 : Quit\n Enter your Choice : ")
            if choice == "3":
                print(p1," points :", pos1)
                print(p2," points :", pos2)
                print("Quitting the game, Thank you for playing !!!")
                break
            elif choice == "2":
                print(p1,"points :", pos1)
                print(p2,"points :", pos2)
                continue
            elif choice == "1":
                pos2 = player_2(pos2, p2)
                if reached_end(pos2):
                    print(p2,"won")
                    break
          
        turn = turn + 1
 
 
# calling functions
show_board()
playgame()