N = int(input())

i = 2
value = []
while True:
    if N % i == 0:
        value.append(i)
        N = N / i
        i = 1
    i += 1

    if N <= 1:
        break
    
for i in range(len(value)):
    print(value[i])