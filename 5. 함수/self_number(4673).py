list = [i for i in range(1,10000)]

for i in range(1,10001):
    d = i
    length = len(str(i))
    for k in range(length):
        d = d + int(str(i)[k])
    if d in list:
        list.remove(d)

for i in range(len(list)):
    print(list[i])