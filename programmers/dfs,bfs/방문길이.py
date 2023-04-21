dxs, dys = [-1, 1, 0, 0], [0, 0, 1, -1]
dir_ = {
    'U': 0,
    'D': 1,
    'R': 2,
    'L': 3
}
visited = [[0] * 11 for _ in range(11)]

def in_range(x, y):
    return 0 <= x < 11 and 0 <= y < 11

def can_go(x, y):
    if not in_range(x, y):
        return False
    return True



def solution(dirs): 
    x, y = 5, 5
    visited[x][y] = 1
    route = set()
    
    for dir in dirs:
        nx, ny = x + dxs[dir_[dir]], y + dys[dir_[dir]]
        if can_go(nx, ny):
            visited[nx][ny] = 1  
            if not ((nx, ny), (x, y)) in route:
                route.add(((x, y), (nx, ny)))
            x, y = nx, ny
            
    route = set(route)
        
    
    answer = len(route)
    return answer
            
