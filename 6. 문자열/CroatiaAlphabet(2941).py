message = input()

count = 0
j = 1

for i in range(len(message)):
    mark = 0
    if len(message) == 1:
        count+=1
        break
    if message[j] == 'j' and message[j-1] == 'l':
        j += 1
        count+=1
        mark = 1
    elif message [j] == '=' and message[j-1] == 'c':
        j += 1
        count+=1
        mark = 1
    elif message [j] == '-' and message[j-1] == 'c':
        j += 1
        count+=1
        mark = 1
    elif message [j] == '=' and message[j-1] == 'z' and message[j-2] == 'd':
        j += 2
        count+=1
        mark = 1
    elif message [j] == '-' and message[j-1] == 'd':
        j += 1
        count+=1
        mark = 1
    elif message [j] == 'j' and message[j-1] == 'n':
        j += 1
        count+=1
        mark = 1
    elif message [j] == '=' and message[j-1] == 's':
        j += 1
        count+=1
        mark = 1
    elif message [j] == '=' and message[j-1] == 'z':
        j += 1
        count+=1
        mark = 1
    else:
        count+=1
    j += 1
    print(j, count)
    if j == len(message) and mark == 0:
        count+=1
        break
    elif j-1 == len(message) and mark == 1:
        break

print(count)