n = int(input())
first_line = list(map(int, input().split()))

another_line, snack_line = [], []

num = 1
while len(snack_line) < n: #while을 한번만 사용하면 되기 때문에 중복된 while이 필요하지 않다.
    if first_line and first_line[0] == num:
        snack_line.append(first_line.pop(0))
        num += 1
    elif another_line and another_line[-1] == num:
        snack_line.append(another_line.pop())
        num += 1
    elif first_line: # 첫번째 줄에서 다음 숫자가 없으면 another_line에 추가
        another_line.append(first_line.pop(0))
    else: # 정해진 순서대로 간식을 받을 수 없는 경우
        print('Sad')
        break
else: # 정해진 순서대로 간식을 받는 경우
    print('Nice')
