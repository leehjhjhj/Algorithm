from collections import deque

def bfs(start):
    visited = [-1 for _ in range(n + 1)]
    queue = deque([start])
    visited[start] = 0
    while queue:
        v = queue.popleft()
        for w, weight in tree[v]:
            if visited[w] == -1:
                visited[w] = visited[v] + weight
                queue.append(w)
    return visited

n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    parents, child, distance = tuple(map(int, input().split()))
    tree[parents].append((child, distance))
    tree[child].append((parents, distance))

result_1st_bfs = bfs(1)
farthest_node_index = result_1st_bfs.index(max(result_1st_bfs))

result_2nd_bfs = bfs(farthest_node_index)
print(farthest_node_index)
print(max(result_2nd_bfs))
farthest_node_index = result_2nd_bfs.index(max(result_2nd_bfs))
print(farthest_node_index)
