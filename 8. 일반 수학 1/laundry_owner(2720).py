import sys

T = int(input())

coin_list = []

for i in range(T):
    C = int(sys.stdin.readline())
    Q, rest = divmod(C , 25)
    D, rest = divmod(rest, 10)
    N, rest = divmod(rest, 5)
    P, rest = divmod(rest, 1)
    
    coin_list.append([Q, D, N, P])

for i in range(T):
    for j in range(4):
        print(coin_list[i][j], end= ' ')
    print()