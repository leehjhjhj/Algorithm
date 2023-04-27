from collections import deque
X, Y = 0, 0
visited = []
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]


def is_range(x, y):
    return 0 <= x < X + 1 and 0 <= y < Y + 1

def can_go(x, y, maps):
    if not is_range(x, y):
        return False
    
    if visited[x][y] or maps[x][y] == 0:
        return False
    return True

def show():
    for visit in visited:
        for i in visit:
            print(i, end=' ')
        print()
    print()

def bfs(q, maps):
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny, maps):
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
        
    
def solution(maps):
    global X
    global Y
    global visited
    X = len(maps) - 1
    Y = len(maps[0]) - 1


    visited = [[0] * (Y + 1) for _ in range(X + 1)] 
    
    q = deque()
    visited[0][0] = 1
    q.append((0, 0))
    bfs(q, maps)
    
    if visited[X][Y] == 0:
        return -1
    
    return visited[X][Y]
