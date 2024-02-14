import sys

N = int(sys.stdin.readline())
len_list = sorted([int(sys.stdin.readline()) for _ in range(N)], reverse=True)

idx = 0

while idx <= len(len_list) - 3:
    if len_list[idx] < len_list[idx+1] + len_list[idx+2]:
        print(len_list[idx] + len_list[idx+1] + len_list[idx+2])
        break
    idx+=1

if idx > len(len_list) - 3:
    print(-1)