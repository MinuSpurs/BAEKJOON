S = input()

substring = []

i, j = 0, 1
cnt = 1
while j <= (len(S) + 1):    
    substring.append(S[i:j])
    i += 1
    j += 1
    if j == len(S) + 1:
        i = 0
        cnt += 1
        j = cnt
        
print(len(set(substring)))