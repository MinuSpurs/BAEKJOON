N = int(input())

value = 666
temp = []


while True:
    if '666' in str(value):
        temp.append(value)
        value += 1
    else:
        value += 1

    if len(temp) == N:
        break

print(temp[N-1])