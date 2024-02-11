## Let's play Tic Tac Toe! #

# Milestone Project 1. Create a Tic Tac Toe Game.
# What the code must be able to do:

# need to print a board.
# Take in player input.
# Place their input on the board.
# Check if the game is won,tied, lost, or ongoing.
# Repeat c and d until the game has been won or tied.
# Ask if players want to play again.

# Author: Jason K Als

# Import Necessary Modules
# To clear the terminal
import os
# To create 'delay' effect on text output
import time
# To Use standard out's 'write' function which will eliminate the default
# newlines created by 'print' function
import sys

# Clear the Screen
os.system('clear')

# Create placeholder (list) for gameboard
board = []
# Remember all of the player's used moves (will be used to determined if a
# move is already taken and will ask player to select a different one)
player_all_moves = []


# Introduction and Player Names
# Receive sentence parameter and display it one letter at a time, flush
# standard out buffer, and display next letter. Wait .02 seconds before
# displaying next letter
def delay_print(sentence):
    os.system('clear')
    for letter in sentence:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)

delay_print("\n\n\t\t\tHello Players! Let's play a game of Tic Tac Toe!")

if '3' in sys.version:
    input("\nPress ENTER ")

delay_print(
    "\n\n\t\t\tThe rules are simple. Players will play on a 3x3 game board.\n\t\t\t player 1 plays as 'X' and Player 2 plays 'O'. To win get 3 of your \n\t\t\tletters in a row either horizontally, vertically, or diagonally\n\n\n")

input("Press ENTER to Continue... ")


# Draw Board
def draw_board():
    for column in range(3):
        board.append([])
        for row in range(3):
            board[column].append('')
# Get player names
draw_board()
os.system('clear')
player1 = input('Player 1 (X) Enter Your Name:  ').title()
while player1 == '' or player1 in '1234567890':
    player1 = input('Player 1 (X) Enter Your Name:  ').title()

player2 = input('Player 2 (O) Enter Your Name:  ').title()
while player2 == '' or player1 in '1234567890':
    player2 = input('Player 2 (O) Enter Your Name:  ').title()

# Print Board


def print_board():
    s = 1
    print('   A', '  B', '  C')
    for row in board:
        print(s, row)
        s += 1


# Determine if game won
def game_won():
    global player1_win
    global player2_win
    
    player1_win = False
    player2_win = False

    def playagain():
        global board
        global player_all_moves
        play_again = input("\nWant to play again?  (Type 'yes' or 'no')  ")
        player_all_moves = []
        board = []
        os.system('clear')
        while True:
            if play_again == 'yes':
                draw_board()
                play_game()
                os.system('clear')
            elif play_again == 'no':
                quit()
            else:
                play_again = input("\nWant to play again?  (Type 'yes' or 'no')  ")
                player_all_moves = []
                board = []
                os.system('clear')

    if 'X' == board[0][0] == board[0][1] == board[0][2]:
        os.system('clear')
        print(player1 + " WINS!!!\n")
        player1_win = True
        print_board()
        playagain()
    elif 'X' == board[1][0] == board[1][1] == board[1][2]:
        os.system('clear')
        print('\n' + player1 + " WINS!!!\n")
        player1_win = True
        print_board()
        playagain()
    elif 'X' == board[2][0] == board[2][1] == board[2][2]:
        os.system('clear')
        print('\n' + player1 + " WINS!!!\n")
        player1_win = True
        print_board()
        playagain()
    elif 'X' == board[0][0] == board[1][0] == board[2][0]:
        os.system('clear')
        print('\n' + player1 + " WINS!!!\n")
        player1_win = True
        print_board()
        playagain()
    elif 'X' == board[0][1] == board[1][1] == board[2][1]:
        os.system('clear')
        print('\n' + player1 + " WINS!!!\n")
        player1_win = True
        print_board()
        playagain()
    elif 'X' == board[0][2] == board[1][2] == board[2][2]:
        os.system('clear')
        print('\n' + player1 + " WINS!!!\n")
        player1_win = True
        print_board()
        playagain()
    elif 'X' == board[0][2] == board[1][1] == board[2][0]:
        os.system('clear')
        print('\n' + player1 + " WINS!!!\n")
        player1_win = True
        print_board()
        playagain()
    elif 'X' == board[0][0] == board[1][1] == board[2][2]:
        os.system('clear')
        print('\n' + player1 + " WINS!!!\n")
        player1_win = True
        print_board()
        playagain()
    elif 'O' == board[0][0] == board[0][1] == board[0][2]:
        os.system('clear')
        print('\n' + player2 + " WINS!!!\n")
        player2_win = True
        print_board()
        playagain()
    elif 'O' == board[1][0] == board[1][1] == board[1][2]:
        os.system('clear')
        print('\n' + player2 + " WINS!!!\n")
        player2_win = True
        print_board()
        playagain()
    elif 'O' == board[2][0] == board[2][1] == board[2][2]:
        os.system('clear')
        print('\n' + player2 + " WINS!!!\n")
        player2_win = True
        print_board()
        playagain()
    elif 'O' == board[0][0] == board[1][0] == board[2][0]:
        os.system('clear')
        print('\n' + player2 + " WINS!!!\n")
        player2_win = True
        print_board()
        playagain()
    elif 'O' == board[0][1] == board[1][1] == board[2][1]:
        os.system('clear')
        print('\n' + player2 + " WINS!!!\n")
        player2_win = True
        print_board()
        playagain()
    elif 'O' == board[0][2] == board[1][2] == board[2][2]:
        os.system('clear')
        print('\n' + player2 + " WINS!!!\n")
        player2_win = True
        print_board()
        playagain()
    elif 'O' == board[0][2] == board[1][1] == board[2][0]:
        os.system('clear')
        print('\n' + player2 + " WINS!!!\n")
        player2_win = True
        print_board()
        playagain()
    elif 'O' == board[0][0] == board[1][1] == board[2][2]:
        os.system('clear')
        print('\n' + player2 + " WINS!!!\n")
        player2_win = True
        print_board()
        playagain()
    elif len(player_all_moves) == 9:
        os.system('clear')
        print('Oh no!' + player1 + ' and ' + player2 + " have tied!!\n\n")
        print_board()
        playagain()
    else:
        pass

# place move on board


def move_on_game_board(player, move):
    if player == player1:
        player_letter = 'X'
    else:
        player_letter = 'O'

    if move == 'A1' and board[0][0] == '':
        board[0][0] = player_letter
    elif move == 'B1' and board[0][1] == '':
        board[0][1] = player_letter
    elif move == 'C1' and board[0][2] == '':
        board[0][2] = player_letter
    elif move == 'A2' and board[1][0] == '':
        board[1][0] = player_letter
    elif move == 'B2' and board[1][1] == '':
        board[1][1] = player_letter
    elif move == 'C2' and board[1][2] == '':
        board[1][2] = player_letter
    elif move == 'A3' and board[2][0] == '':
        board[2][0] = player_letter
    elif move == 'B3' and board[2][1] == '':
        board[2][1] = player_letter
    elif move == 'C3' and board[2][2] == '':
        board[2][2] = player_letter


def play_game():
    choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

    def save_moves():
        if player1_move in choices and player1_move not in player_all_moves:
            player_all_moves.append(player1_move)
            move_on_game_board(player1, player1_move)
            game_won()
        elif player2_move in choices and player2_move not in player_all_moves:
            player_all_moves.append(player2_move)
            move_on_game_board(player2, player2_move)
            game_won()
            play_game()
        else:
            pass

    print_board()
    player1_move = input(player1 + ", got for it  ").capitalize()

    while player1_move not in choices or player1_move in player_all_moves:
        if player1_move not in choices:
            player1_move = input(
                player1 + ", please make a valid move. For example: 'a1'  ").capitalize()
            print_board()
        elif player1_move in player_all_moves:
            player1_move = input(
                player1 + ", " + player1_move + " is already taken. Try somewhere else  ").capitalize()
            print_board()
        else:
            pass

    save_moves()
    print_board()

    player2_move = input(player2 + ", got for it  ").capitalize()

    while player2_move not in choices or player2_move in player_all_moves:
        if player2_move not in choices:
            player2_move = input(
                player2 + ", please make a valid move. For example: 'a1'  ").capitalize()
            print_board()
        elif player2_move in player_all_moves:
            player2_move = input(
                player2 + ", " + player2_move + " is already taken. Try somewhere else  ").capitalize()
            print_board()
        else:
            pass

    save_moves()


play_game()
print(player_all_moves)
