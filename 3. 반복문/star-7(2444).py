s = int(input())

for i in range(s):
    print(' ' * (s - i - 1) + '*' * (i * 2 + 1))

for i in range(s-2, -1, -1):
    print(' ' * (s - i - 1) + '*' * (i * 2 + 1))