N = int(input())
count = 0

for i in range(1,N+1):
    temp = []
    length = len(str(i))   
    if length <= 2:
        count+=1
    for j in range(length-1):
        temp.append(int(str(i)[j]) - int(str(i)[j+1]))
        num = temp[0]
    for k in range(len(temp)-1):   
        if len(temp) >= 2 and num != temp[k+1]:
            break
        else:
            count+=1

print(count)