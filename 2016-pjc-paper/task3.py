#!/usr/bin/env python3

def display_board(board):
    PRINT_FORMAT = '{:2}'
    print()
    for i in range(3):
        for j in range(3):
            mark = board[i * 3 + j]
            if mark is None:
                print(PRINT_FORMAT.format(''), end='')
            else:
                print(PRINT_FORMAT.format(mark), end='')
        print()

def display_instructions():
    print('=== How to play the game ===')
    print('The program will prompt for 3 inputs - row no. and column no.')
    print()
    print('The prompt format is as follows:')
    print('--Player 1\'s turn--')
    print('Enter a row no. (1 - 3): 1')
    print('Enter a column no. (1 - 3): 3')
    print()
    print('In the example above, player 1 marks an X on the tile at row 1, column 3.')
    print('In the case of player 2, an O will be marked instead.')
    print()
    print('That\'s all. Have fun!')
    print()
    print()

def get_player_move(board, mark):
    VALID_INPUTS = ['1', '2', '3']

    row = input('Enter a row no. (1 - 3): ')
    while row not in VALID_INPUTS:
        print()
        print('Invalid row no. Please enter a row no. from 1 - 3.')
        row = input('Enter a row no. (1 - 3): ')
    col = input('Enter a column no. (1 - 3): ')
    while col not in VALID_INPUTS:
        print()
        print('Invalid col no. Please enter a col no. from 1 - 3.')
        col = input('Enter a col no. (1 - 3): ')

    row = int(row)
    col = int(col)

    index = (row - 1) * 3 + (col - 1)
    if board[index] is not None:
        print('Failed to mark the tile as it is currently occupied.')
    else:
        board[index] = mark

def check_win(board):
    conditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    for first, second, third in conditions:
        if board[first] is not None and \
                board[first] == board[second] and \
                board[second] == board[third]:
            return True
    return False

def main():
    display_instructions()

    cur_player = input('Which player starts first? (1 or 2): ')
    while cur_player != '1' and cur_player != '2':
        print('Invalid player no. Please choose either player 1 or 2 to start first.')
        cur_player = input('Which player starts first? (1 or 2): ')
    cur_player = int(cur_player)

    board = [None] * 9

    while not check_win(board) and None in board:
        print()
        print()
        print('--Player {}\'s turn--'.format(cur_player))
        get_player_move(board, 'X' if cur_player == 1 else 'O')
        display_board(board)
        cur_player = 1 if cur_player == 2 else 2

    print()
    if check_win(board):
        winner = 1 if cur_player == 2 else 2
        print('Player {} won!'.format(winner))
    else:
        print('The game ended in a draw.')

main()
