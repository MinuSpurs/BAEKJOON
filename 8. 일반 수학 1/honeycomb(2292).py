N = int(input())

result = 1
temp = 6


while N > 1:
    N -= temp
    temp += 6
    result += 1

print(result)