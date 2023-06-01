x = int(input())

up, down = 1, 1
pin = 0
max_value = 2
up_point, down_point = 0, 1

for i in range(x-1):
    if down_point == 1:
        down_point = 0
        down += 1
        pin = 1
    elif up_point == 1:
        up_point = 0
        up += 1
        pin = 2
    elif down_point == 0 and pin == 1:
        up += 1
        down -= 1
        if up == max_value:
            up_point = 1
            max_value += 1
    else:
        down += 1
        up -= 1
        if down == max_value:
            down_point = 1
            max_value += 1

print(str(up)+'/'+str(down))