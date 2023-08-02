import sys

n = int(input())
stk = []

for i in range(n):
    oper = sys.stdin.readline().rstrip()
    if oper[:1] == '1':
        stk.append(int(oper[2:]))
    elif oper == '2':
        if len(stk) == 0:
            print(-1)
        else:
            print(stk.pop())
    elif oper == '3':
        print(len(stk))
    elif oper == '4':
        if len(stk) == 0:
            print(1)
        else:
            print(0)
    elif oper == '5':
        if len(stk) == 0:
            print(-1)
        else:
            print(stk[-1])