n = int(input())

couple = int(input())

graph = [[] for _ in range(n+1)]

for i in range(couple):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x, count):
    visited[x] = True
    for node in graph[x]:
        if not visited[node]:
            count = dfs(node, count+1)
    return count

visited = [False] * (n+1)
print(dfs(1, 0))