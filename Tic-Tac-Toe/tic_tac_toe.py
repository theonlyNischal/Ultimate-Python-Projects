def display_board(board):
    print(board[7] + "|" + board[8] + "|" + board[9])
    print(board[4] + "|" + board[5] + "|" + board[6])
    print(board[1] + "|" + board[2] + "|" + board[3])


the_board = [' '] * 10

if __name__ == '__main__':
    display_board(the_board)