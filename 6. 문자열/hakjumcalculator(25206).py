import sys

array = []
plus = 0
for i in range(20):
    name, hak, score = map(str, sys.stdin.readline().split())
    plus += float(hak)
    if score == 'A+':
        float_score = 4.5
    elif score == 'A0':
        float_score = 4.0
    elif score == 'B+':
        float_score = 3.5
    elif score == 'B0':
        float_score = 3.0
    elif score == 'C+':
        float_score = 2.5
    elif score == 'C0':
        float_score = 2.0
    elif score == 'D+':
        float_score = 1.5
    elif score == 'D0':
        float_score = 1.0
    elif score == 'F':
        float_score = 0.0
    else:
        plus -= float(hak)
        continue
    array.append(float(hak) * float_score)

result = 0
for i in range(len(array)):
    result += array[i]

print(result/plus)

