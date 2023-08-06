from collections import deque

n, k = map(int, input().split())

queue = deque([i + 1 for i in range(n)])
jose = []

while queue:
    for _ in range(k - 1): 
        queue.append(queue.popleft())
    
    jose.append(queue.popleft())

print("<" + ", ".join(map(str, jose)) + ">") 
