def display_board(board):
    print("+-----+-----+-----+")
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print("  {}  |".format(board[i][j]), end="")
        print("\n+-----+-----+-----+")


board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
display_board(board)
