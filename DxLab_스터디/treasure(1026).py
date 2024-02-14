import sys

N = int(sys.stdin.readline())
a_list = sorted(list(map(int,sys.stdin.readline().split())))
b_list = sorted(list(map(int,sys.stdin.readline().split())), reverse=True)

result = 0

for i in range(N):
    result += (a_list[i] * b_list[i])

print(result)