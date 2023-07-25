import sys

k = int(input())
num_list = []
result = 0

for i in range(k):
    num = int(sys.stdin.readline())
    if num != 0:
        num_list.append(num)
        result += num
    elif num == 0:
        result -= num_list.pop()

print(result)