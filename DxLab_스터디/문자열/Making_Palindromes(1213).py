name = input()
counter = [0]*26

for char in name:
    counter[ord(char)-ord('A')] += 1

odd = [i for i in range(26) if counter[i]%2]
if len(odd) > 1:
    print("I'm Sorry Hansoo")
else:
    first_half = [chr(i+ord('A'))*(counter[i]//2) for i in range(26)]
    if odd:
        center = chr(odd[0]+ord('A'))
    else:
        center = ''
    print(''.join(first_half) + center + ''.join(first_half[::-1]))