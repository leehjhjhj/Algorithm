import sys
from collections import deque
sys.setrecursionlimit(10**6)

n = int(input())
city = []
max_height = 0
safe_zone = 0

def bfs(i, j, graph):
    global cnt
    q = deque()
    q.append((i, j))
    graph[i][j] = True
    while q:
        x_t, y_t = q.popleft()
        for dx, dy in (0, 1), (0, -1), (-1, 0), (1, 0):
            x, y = dx + x_t, dy + y_t
            if  0 <= x < n and 0 <= y < n and graph[x][y] == False and city[x][y] > height:
                    q.append((x, y))
                    graph[x][y] = True

for _ in range(n):
    input_arr = list(map(int, input().split()))
    target = max(input_arr)
    if target >= max_height:
        max_height = target
    city.append(input_arr)

for height in range(max_height + 1):
    graph = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if city[i][j] > height and graph[i][j] == False:
                bfs(i, j, graph)
                cnt += 1

    if cnt >= safe_zone:
        safe_zone = cnt

    cnt = 0

print(safe_zone)
