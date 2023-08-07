import sys
from collections import deque

n = int(input())

queue = deque([])

for i in range(n):
    op = input()

    if op[:1] == '1':
        queue.insert(0, int(op[2:]))
    elif op[:1] == '2':
        queue.insert(len(queue), op[2:])
    elif op == '3':
        print(-1 if len(queue) == -1 else queue.popleft())
    elif op == '4':
        print(-1 if len(queue) == -1 else queue.pop())
    elif op == '5':
        print(len(queue))
    elif op == '6':
        print(1 if len(queue) == 0 else 0)
    elif op == '7':
        print(-1 if len(queue) == 0 else queue[0])
    elif op == '8':
        print(-1 if len(queue) == 0 else queue[-1])