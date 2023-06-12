import sys

value = []
avg = 0

for i in range(5):
    num = int(sys.stdin.readline())
    value.append(num)
    avg += num

for i in range(4, 0, -1):
    for j in range(i):
        if value[j] > value[j+1]:
            temp = value[j]
            value[j] = value[j+1]
            value[j+1] = temp

print(int(avg/5))
print(value[2])
