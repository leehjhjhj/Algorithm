from collections import deque

n ,m ,t = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
have_sword = False
sword_result = 0
q = deque()
result = 0



def is_range(x, y):
    return 0 <= x < n and 0 <= y < m

def is_sword(x, y):
    return is_range(x, y) and grid[x][y] == 2

def can_go(x, y):
    if not is_range(x, y):
        return False
    if visited[x][y] != 0 or grid[x][y] == 1:
        return False
    return True

dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs():
    global sword_result, have_sword
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if not have_sword and is_sword(nx, ny):
                have_sword = True
                sword_result = (n - 1 - nx) + (m - 1 - ny) + visited[x][y] + 1
            if can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

def show():
    print()
    for row in visited:
        print(*row)


q.append((0,0))
visited[0][0] = 1
bfs()

if visited[n-1][m-1] == 0:
    if sword_result == 0:
        print("Fail")
    elif sword_result -1 <= t:
        print(sword_result - 1)
    else:
        print("Fail")
else:
    resultt = min(sword_result, visited[n-1][m-1]) -1
    if resultt <= t:
        print(resultt)
    else:
        print("Fail")