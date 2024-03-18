import sys
from collections import deque

def bfs(graph, start, visited, cnt):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    cnt += 1
    return cnt

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

visited = [False] * n

cnt = 0
idx = 0

while False in visited:
    if visited[idx] == False:
        cnt = bfs(graph, idx, visited, cnt)
    idx += 1

print(cnt)