a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

if abs(a1) * n0 + abs(a0) <= c * n0:
    print('1')
else:
    print('0')