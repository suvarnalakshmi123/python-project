from random import randrange
def display_board(board):
    print("+-----+-----+-----+")
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print("  {}  |".format(board[i][j]), end="")
        print("\n+-----+-----+-----+")


board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
display_board(board)

def enter_move(board):
    ok = False
    while not ok:
        move=input("enter your move:")
        ok=len(move)==1 and move>="1" and move<="9"
        if not ok:
            print("bad input")
            continue
        move=int(move)-1
        row=move//3
        col=move%3
        sign=board[row][col]
        print(sign)
        ok=sign not in ["X","O"] 
        if not ok:
            print("It is occupied repeat your input")
            continue
    board[row][col]="O" 


def make_list_of_free_fields(board):
    free = []
    for i in range(3): 
        for j in range(3):
            if board[i][j] not in ['X', 'O']:
                free.append((i, j))
    return free()

def draw_move(board):
    free = make_list_of_free_fields(board)
    counter = len(free)
    if counter > 0:
        it = randrange(counter)  
        row,col = free[it]
        print(row,col)
    draw_move(board)  
