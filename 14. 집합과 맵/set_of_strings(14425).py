import sys

N ,M = map(int, input().split())

set_list = []
string_list = []
count = 0

for i in range(N):
    temp = sys.stdin.readline().rstrip()
    set_list.append(temp)

for i in range(M):
    temp = sys.stdin.readline().rstrip()
    string_list.append(temp)

for i in range(M):
    if string_list[i] in set(set_list):
        count += 1

print(count)