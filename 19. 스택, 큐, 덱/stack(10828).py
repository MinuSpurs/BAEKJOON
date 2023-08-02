import sys

n = int(input())
stk = []

for i in range(n):
    oper = sys.stdin.readline().rstrip()
    if oper[:4] == 'push':
        stk.append(int(oper[5:]))
    elif oper == 'pop':
        if len(stk) == 0:
            print(-1)
        else:
            print(stk.pop())
    elif oper == 'size':
        print(len(stk))
    elif oper == 'empty':
        if len(stk) == 0:
            print(1)
        else:
            print(0)
    elif oper == 'top':
        if len(stk) == 0:
            print(-1)
        else:
            print(stk[-1])