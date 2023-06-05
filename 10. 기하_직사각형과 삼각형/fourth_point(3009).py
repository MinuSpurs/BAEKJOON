import sys

value = []

for i in range(3):
    x = list(map(int, sys.stdin.readline().split()))
    value.append(x)

x1, y1 = value[0][0], value[0][1]

x1_cnt, y1_cnt = 0, 0

for i in range(3):
    if x1 == value[i][0]:
        x1_cnt += 1
    else:
        x2 = value[i][0]

    if y1 == value[i][1]:
        y1_cnt += 1
    else:
        y2 = value[i][1]

if x1_cnt == 2:
    x3 = x2
else:
    x3 = x1

if y1_cnt == 2:
    y3 = y2
else:
    y3 = y1
    
print(x3, y3)