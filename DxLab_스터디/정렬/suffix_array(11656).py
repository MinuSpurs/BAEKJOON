s = input()

arr = [s[i:] for i in range(len(s))]

for i in range(len(s)):
    print(sorted(arr)[i])