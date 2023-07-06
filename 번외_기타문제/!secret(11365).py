import sys

while True:
    a = sys.stdin.readline().rstrip()
    temp = []
    if a == 'END':
        break
    print(a[::-1])