T = int(input())
output = []

for i in range(T):
    R, S = map(str, input().split())
    R = int(R)
    temp = ''
    for j in range(len(S)):       
        temp += S[j]*R
    output.append(temp)

for i in range(len(output)):
    print(output[i])