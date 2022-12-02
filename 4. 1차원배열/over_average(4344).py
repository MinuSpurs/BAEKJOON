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
    print(f'{count/test[i][0]*100:.3f}%')