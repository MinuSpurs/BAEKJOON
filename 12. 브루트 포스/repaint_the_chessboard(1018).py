import sys

N, M = map(int, input().split())
board_list = []
for i in range(N):
    board = list(sys.stdin.readline().rstrip())
    board_list.append(board)

x_board = []
cnt = 0

for i in range(8):
    y_board = []
    for j in range(8):
        y_board.append(board_list[i][j])
    x_board.append(y_board)

for i in range(8):
    for j in range(8):
        if i == 1 and j == 1 and (x_board[i][j] == 'B' and x_board[i][j+1] != 'W' and x_board[i+1][j] != 'W'):
            if 
        elif i == 1 and j != 7 and j != 1 and (x_board[i][j] == 'B' and x_board[i][j+1] != 'W' and x_board[i][j-1] != 'W' and x_board[i+1][j] != 'W'):

        elif i != 7 and j != 7 and (x_board[i][j] == 'B' and x_board[i][j+1] != 'W' and x_board[i+1][j] != 'W'):


print(x_board)