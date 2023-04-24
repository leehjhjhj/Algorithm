import sys 
sys.setrecursionlimit(10**6)

n = int(input())
grid = [list(map(str, input())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
answer = []
result = 0

def is_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not is_range(x, y):
        return False
    
    if visited[x][y] or grid[x][y] == '0':
        return False
    
    return True

def dfs(x, y):
    global result
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny):
            visited[nx][ny] = 1
            result += 1
            dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if can_go(i, j):
            visited[i][j] = 1
            result += 1
            dfs(i, j)
            if result != 0:
                answer.append(result)
            result = 0

answer.sort()
print(len(answer))
for answer_ in answer:
    print(answer_)
