s = input()

for i in range(len(s)):
    if s[i] == s[len(s)-i-1]:
        if i == len(s)-1:
            print("1")
            break
        continue
    else:
        print("0")
        break
