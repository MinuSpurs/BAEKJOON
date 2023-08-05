from collections import deque

n = int(input())

card = deque([])

for i in range(1, n+1):
    card.append(i)

for i in range(n):
    if len(card) != 1:
        card.popleft()
        card.append(card.popleft())
    else:
        break

print(*card)