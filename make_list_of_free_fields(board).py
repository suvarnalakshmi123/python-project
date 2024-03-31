def make_list_of_free_fields(board):
    free = []
    for i in range(3): 
        for j in range(3):
            if board[i][j] not in ['X', 'O']:
                free.append((i, j))
    return free()