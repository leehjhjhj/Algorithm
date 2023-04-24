import sys
from collections import deque
input = sys.stdin.readline
q = deque()

n, m = tuple(map(int, input().split()))
relation = [[] for _ in range(n+1)]
count = 0
result = 0
results = [0]
visited = [0] * (n + 1)
for _ in range(m):
    a, b = tuple(map(int, input().split()))
    relation[b].append(a)

def bfs():
    global count
    while q:
        i = q.popleft()
        for v in relation[i]:
            if visited[v] == 0:
                count += 1
                visited[v] = 1
                q.append(v)


for i in range(1, n + 1):
    q.append(i)
    count += 1
    visited[i] = 1
    bfs()
    results.append(count)
    visited = [0] * (n + 1)
    count = 0

max_ = max(results)
print(*[i for i in range(1, n + 1) if results[i] == max_])
