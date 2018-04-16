import random
def display_board(board):
    print(board[7] + "|" + board[8] + "|" + board[9])
    print(board[4] + "|" + board[5] + "|" + board[6])
    print(board[1] + "|" + board[2] + "|" + board[3])

def player_marker():
    if random.randint(0,1) == 0:
        return ('X', 'O', 'Player 1')
    else:
        return ('O', 'X', 'Player 2')

def empty_space(board, position):
    if board[position] == ' ':
        return True
    else:
        return False


def player_input(board):
    position = 0
    while position not in list(range(1,10)) or not empty_space(board, position):
        position = int(input("Enter a valid number to fill the board: "))
    return position

def fill_board(board, position, player_marker):
    board[position] = player_marker

def check_player_won(board, player_marker):
    WIN_COMBINATIONS = [
        (1,2,3), (4,5,6), (7,8,9),
        (1,4,7), (2,5,8), (3,6,9),
        (1,5,9), (3,5,7)
    ]

    for x,y,z in WIN_COMBINATIONS:
        if board[x] == board[y] == board[z] == player_marker:
            return True
    return False

def check_game_draw(board):
    for i in range(1, 10):
        if empty_space(board, i):
            return False

    return True

def play_again():
    return input("Enter 'Y' or 'y' to play again: ").lower().startswith('y')




if __name__ == '__main__':
    while True:
        gameOn = True
        the_board = [' '] * 10
        # Welcome message
        print("Welcome to the world of Tic Tac Toe")
        # Players Marker
        player1_marker, player2_marker,turn = player_marker()
        print("Player 1 will have {player1} \nPlayer 2 will have {player2}".format(player1=player1_marker, player2=player2_marker))
        # Who will go first
        print("{first} will go first.".format(first=turn))
        # While Game is On:
        while gameOn:
            if turn == 'Player 1':
                display_board(the_board)
                print("{player} turn with marker {marker}".format(player=turn, marker=player1_marker))
                position = player_input(the_board)
                fill_board(the_board, position, player1_marker)
                if check_player_won(the_board, player1_marker):
                    display_board(the_board)
                    print("Congratulations! Player 1 Won!!")
                    gameOn = False
                elif check_game_draw(the_board):
                    display_board(the_board)
                    print("Game is Tie")
                    gameOn = False
                else:
                    turn = 'Player 2'
            else:
                display_board(the_board)
                print("{player} turn with marker {marker}".format(player=turn, marker=player2_marker))
                position = player_input(the_board)
                fill_board(the_board, position, player2_marker)
                if check_player_won(the_board, player2_marker):
                    display_board(the_board)
                    print("Congratulations! Player 2 Won!!")
                    gameOn = False
                elif check_game_draw(the_board):
                    display_board(the_board)
                    print("Game is Tie")
                    gameOn = False
                else:
                    turn = 'Player 1'
        if not play_again():
            break