import sys

value = 1
for i in range(3):
    num = int(sys.stdin.readline())
    value *= num

array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(str(value))):
    array[int(str(value)[i])] += 1

for i in range(len(array)):
    print(array[i])