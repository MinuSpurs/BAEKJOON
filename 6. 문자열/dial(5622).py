message = input()

time = 0
for i in range(len(message)):
    if ord(message[i]) >= 65 and ord(message[i]) <= 67:
        time += 3
    elif ord(message[i]) >= 68 and ord(message[i]) <= 70:
        time += 4
    elif ord(message[i]) >= 71 and ord(message[i]) <= 73:
        time += 5
    elif ord(message[i]) >= 74 and ord(message[i]) <= 76:
        time += 6
    elif ord(message[i]) >= 77 and ord(message[i]) <= 79:
        time += 7
    elif ord(message[i]) >= 80 and ord(message[i]) <= 83:
        time += 8
    elif ord(message[i]) >= 84 and ord(message[i]) <= 86:
        time += 9
    elif ord(message[i]) >= 87 and ord(message[i]) <= 90:
        time += 10

print(time)