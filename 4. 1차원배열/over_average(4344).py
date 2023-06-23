def avg_round(value):
    avg = int(value * 10000)
    if avg % 10 >= 5:
        avg += 10
    result = (avg // 10) / 1000
    return result

C = int(input())
test,avg = [],[]


for i in range(C):
    test.append(list(map(int, input().split())))
    temp = 0
    for j in range(1, len(test[i])):
        temp+=test[i][j]
    avg.append(temp/test[i][0])

for i in range(C):
    count = 0
    for j in range(1,len(test[i])):
        if test[i][j] > avg[i]:
            count+=1

    print(f'{avg_round(count/test[i][0]*100):.3f}%')