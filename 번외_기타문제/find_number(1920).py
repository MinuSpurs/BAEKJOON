import sys

N = int(input())
num_dict = {}
temp = list(map(int, input().split()))

for i in range(N):
    num_dict[temp[i]] = i

M = int(input())
m_list = list(map(int, input().split()))

for i in range(M):
    if m_list[i] in num_dict:
        print(1)
    else:
        print(0)