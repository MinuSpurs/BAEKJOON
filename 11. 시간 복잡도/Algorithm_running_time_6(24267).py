n = int(input())

result = 0
count = 2

for i in range(1, n-1):
    result += i * (n-count)
    count += 1

print(result)
print('3')