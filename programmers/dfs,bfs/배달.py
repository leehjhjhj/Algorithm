import sys
from collections import deque



def solution(N, roads, K):
    grid = [[] for _ in range(N + 1)]
    visited = [float('inf')] * (N + 1)

    
    for a, b, c in roads:
        grid[a].append((b, c))
        grid[b].append((a, c))
    print(grid)
    
    def bfs():
        while q:
            v, v_distance = q.popleft()
            if v_distance > visited[v]:
                continue
            for n, n_distance in grid[v]:
                if v_distance + n_distance < visited[n]:
                    visited[n] = v_distance + n_distance
                    q.append((n, visited[n]))
    q = deque() 
    q.append((1,0))
    visited[1] = 0

    bfs()
    print(visited)
    outputs = 0
    
    for target in visited:
        if target <= K:
            outputs += 1
    return outputs
