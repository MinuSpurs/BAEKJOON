import sys

set_list = {}

for y in range(61):
    for x in range(y+1):
        set_list[(1 << x) + (1 << y)] = x,y
        
n = int(input())
for i in range(n):
    temp = int(sys.stdin.readline())
    print(*set_list[temp])