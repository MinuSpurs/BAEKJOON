N = input()
count=0
if int(N)<10:
    A = 0
    B = int(N)
else:
    A = int(N[0])
    B = int(N[1])

while True:
    result = A+B
    
    if result >= 10:
        result-=10

    sub_result = int(str(B)+str(result))

    if sub_result == int(N):
        count+=1
        break
    else:
        count+=1
        A = B
        B = result

print(count)