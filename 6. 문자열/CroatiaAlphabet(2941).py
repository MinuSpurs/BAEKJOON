s = input()

count = 0
i = 0
while i < len(s):
    if s[i:i+2] in ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']:
        count += 1
        i += 2
    elif s[i:i+3] == 'dz=':
        count += 1
        i += 3
    else:
        count += 1
        i += 1

print(count)
