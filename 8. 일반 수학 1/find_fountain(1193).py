x = int(input())

up, down = 1, 1
point = 1
max_up, max_down = 1, 1
pin = 1
for i in range(x-1):
    if point % 2 == 0 and pin == 1:
        print('짝수 핀 1')
        max_up += 1
        up += 1
        pin = 0
        point += 1
        continue
    elif point % 2 == 1 and pin == 1:
        print('홀수 핀 1')
        max_down += 1
        down += 1
        pin = 0
        point += 1
        continue

    if down > up:
        down -= 1
        up += 1
        if (max_up == point) and max_up % 2 == 1:
            pin = 1
    elif up > down:
        up -= 1
        down += 1
        if (max_down == point) and max_down % 2 == 0:
            pin = 1

    
    print(point, max_up, max_down, up, down)

print(str(up)+'/'+str(down))