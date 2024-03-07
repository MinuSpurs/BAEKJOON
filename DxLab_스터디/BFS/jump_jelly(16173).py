from collections import deque 

n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 1]
dy = [1, 0]

def bfs(x, y):    
    queue = deque()
    queue.append((x, y))
    visited = [[False]*n for _ in range(n)]
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        jump = graph[x][y]
        if jump == -1:
            return "HaruHaru"
        for i in range(2):
            nx = x + dx[i] * jump
            ny = y + dy[i] * jump
            if nx < n and ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
    return "Hing"

print(bfs(0, 0))