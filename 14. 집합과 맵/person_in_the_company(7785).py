import sys

person = {}
for _ in range(int(input())):
    temp = list(sys.stdin.readline().split())
    person[temp[0]] = temp[1]

sorted_person = sorted(person, reverse=True)

for key in sorted_person:
    if person[key] != 'leave':
        print(key)