import sys

s = sys.stdin.readline()
target = 'UCPC'
idx = 0

for i in s:
    if target[idx] == i:
        idx+=1
        if idx == 4:
            break

if idx == 4:
    print('I love UCPC')
else:
    print('I hate UCPC')