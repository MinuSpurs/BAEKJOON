T = input().upper()
Max_count = 0
same_count = 0
Max_alpha = ''
place = [0 for i in range(26)]

for i in range(26):
    place[i] = T.count(chr(65+i))

for i in range(len(place)):
    if place[i] > Max_count:
        Max_count = place[i]
        Max_alpha = chr(i+65)
        same_count = 0
    elif place[i] == Max_count:
        same_count = 1

if same_count == 1:
    print("?")
else:
    print(Max_alpha)