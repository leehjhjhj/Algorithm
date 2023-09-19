import sys
sys.setrecursionlimit(10**7)

n = int(input())
mom = [0 for _ in range(n + 1)]
tree = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(n - 1):
    x, y = tuple(map(int, input().split()))
    tree[x].append(y)
    tree[y].append(x)

def dfs(v):
    visited[v] = True
    for i in tree[v]:
        if visited[i] == False:
            visited[v] = True
            mom[i] = v
            dfs(i)

dfs(1)

for i in mom[2:]:
    print(i)
