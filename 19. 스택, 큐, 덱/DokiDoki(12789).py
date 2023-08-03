n = int(input())
first_line = list(map(int, input().split()))

another_line, snack_line = [], []

num = 1
while len(snack_line) < n:
    if first_line and first_line[0] == num:
        snack_line.append(first_line.pop(0))
        num += 1
    elif another_line and another_line[-1] == num:
        snack_line.append(another_line.pop())
        num += 1
    elif first_line:
        another_line.append(first_line.pop(0))
    else:
        print('Sad')
        break
else:
    print('Nice')
