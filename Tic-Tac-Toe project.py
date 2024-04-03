from random import randrange
def display_board(board):
    print("+-----+-----+-----+")
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print("  {}  |".format(board[i][j]), end="")
        print("\n+-----+-----+-----+")


def enter_move(board):
    ok = False
    while not ok:
        move=input("enter your move:")
        ok=len(move)==1 and move>="1" and move<="9"
        if not ok:
            print("bad input - repeat your input")
            continue
        move=int(move)-1
        row=move//3
        col=move%3
        sign=board[row][col]
        print(sign)
        ok=sign not in ["X","O"]
        if not ok:
            print("Field already occupied repeat your input")
            continue
    board[row][col]="O"


def make_list_of_free_fields(board):
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X', 'O']:
                free.append((row, col))
    return free

def victory_for(board,sign):
	if sign == "X":
		who = 'me'
	elif sign == "O":
		who = 'you'
	else:
		who = None
	cross1 = cross2 = True
	for rc in range(3):
		if board[rc][0] == sign and board[rc][1] == sign and board[rc][2] == sign:
			return who
		if board[0][rc] == sign and board[1][rc] == sign and board[2][rc] == sign:
			return who
		if board[rc][rc] != sign:
			cross1 = False
		if board[2 - rc][2 - rc] != sign:
			cross2 = False
	if cross1 or cross2:
		return who
	return None

def draw_move(board):
    free = make_list_of_free_fields(board)
    counter = len(free)
    if counter > 0:
        this = randrange(counter)
        row,col = free[this]
        board[row][col]='X'
        
board = [ [3 * j + i + 1 for i in range(3)] for j in range(3)]

ro = randrange(3)
co = randrange(3)
board[ro][co] = 'X'
free = make_list_of_free_fields(board)
humanturn = True
while len(free):
	display_board(board)
	if humanturn:
		enter_move(board)
		victor = victory_for(board,'O')
	else:
		draw_move(board)
		victor = victory_for(board,'X')
	if victor != None:
		break
	humanturn = not humanturn
	free = make_list_of_free_fields(board)

display_board(board)
if victor == 'you':
	print("You won!")
elif victor == 'me':
	print("I won")
else:
	print("Tie!")
