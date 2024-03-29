def display_board():
  print("+----+----+----+")
  for i in range(3):
      print("|    |    |    |\n|    |    |    |\n|    |    |    |")
      print("+----+----+----+")
display_board()
def make_list_of_free_fields(board):
    free = []
    for i in range(3): 
        for j in range(3):
            if board[i][j] not in ['X', 'O']:
                free.append((i, j))
    return free()
