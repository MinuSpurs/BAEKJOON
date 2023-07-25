import sys

t = int(input())

for i in range(t):
    ps = sys.stdin.readline().rstrip()
    ps_list = []
    if len(ps) % 2 != 0:
        print('NO')
        continue
    for j in range(len(ps)):
        if ps[j] == '(':
            ps_list.append(ps[j])
        else:
            if len(ps_list) == 0:
                ps_list.append(ps[j])
                break
            else:
                ps_list.pop()
    
    print('YES' if len(ps_list) == 0 else 'NO')