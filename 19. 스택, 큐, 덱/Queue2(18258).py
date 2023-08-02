import sys
from collections import deque

n = int(input())

queue = deque([])

for i in range(n):
    oper = sys.stdin.readline().rstrip()
    if oper[:4] == 'push':
        queue.append(int(oper[4:]))

    elif oper == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())

    elif oper == 'size':
        print(len(queue))

    elif oper == 'empty':
        print(1 if len(queue) == 0 else 0)

    elif oper == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    elif oper == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
            