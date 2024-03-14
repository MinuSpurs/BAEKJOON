from collections import deque

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    shape = 1
    graph[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            shape += 1
            queue.append((nx, ny))
            graph[nx][ny] = 0 

    return shape

picture_count = 0
max_picture_area = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            picture_count += 1
            area = bfs(i, j)
            max_picture_area = max(max_picture_area, area)

print(picture_count)
print(max_picture_area)