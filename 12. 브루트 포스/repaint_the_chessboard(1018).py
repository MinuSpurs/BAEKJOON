import sys

b_board = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
w_board = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']

N, M = map(int, input().split())
board_list = []
cnt = []
temp = 0

for i in range(N):
    board = list(sys.stdin.readline().rstrip())
    board_list.append(board)

for t in range(N - 7):
    for i in range(M - 7):
        for j in range(8):
            for k in range(8):
                if (j + t) % 2 == 0 and board_list[j+t][k+i] != b_board[k]:
                    temp += 1
                elif (j + t) % 2 == 1 and board_list[j+t][k+i] != w_board[k]:
                    temp += 1         
    
        cnt.append(temp)
        temp = 0

for t in range(N - 7):
    for i in range(M - 7):
        for j in range(8):
            for k in range(8):
                if (j + t) % 2 == 0 and board_list[j+t][k+i] != w_board[k]:
                    temp += 1
                elif (j + t) % 2 == 1 and board_list[j+t][k+i] != b_board[k]:
                    temp += 1
        cnt.append(temp)
        temp = 0

print(min(cnt))