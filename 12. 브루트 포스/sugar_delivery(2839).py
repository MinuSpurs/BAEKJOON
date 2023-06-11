N = int(input())


division = int(N / 5)
rest = N % 5
k = 1


while True:
    if division == 0 and rest % 3 != 0:
        cnt = -1
        break
    elif rest == 0:
        cnt = division
        break
    elif rest % 3 == 0:
        if 5 * k < rest:
            cnt = N / 3
            break
        else:
            cnt = division + int(rest/3)
            break
    else:
        division -= 1
        rest += 5
        k += 1
        
print(cnt)