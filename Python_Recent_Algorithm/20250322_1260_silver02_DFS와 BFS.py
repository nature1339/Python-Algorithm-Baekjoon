import sys
input = sys.stdin.readline

def dfs(k):
    visited[k] = True
    print(k, end=' ')
    for i in sorted(graph[k]):
        if visited[i] == False:
            dfs(i)

def bfs(k):
    queue = [k]
    visited[k] = True
    while queue:
        vertex = queue.pop(0)
        print(vertex, end=' ')
        for i in sorted(graph[vertex]):
            if visited[i] == False:
                visited[i] = True
                queue.append(i)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n + 1)
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)