import heapq
import sys

input = sys.stdin.readline # 안 하면 시간초과

def dijkstra(start, graph, n):
    distances = [float('inf')] * (n + 1) # 노드까지 도달하는데 최단거리 리스트
    distances[start] = 0
    q = []
    heapq.heappush(q, [0, start]) # 앞에(노드에) distance를 둔다. (heapq를 위해)

    while q:
        curr_distance, curr_node = heapq.heappop(q)
        if distances[curr_node] < curr_distance: # 꺼낸 거리가 현재 노드의 최단거리보다 클 때를 제외.
            continue                             # 다른 경로로 올 수 있기 때문

        for n, n_time in graph[curr_node]:
            distance = curr_distance + n_time # 지금까지의 거리 + 새로운 노드의 거리
            if distance < distances[n]: # 그 거리가 현재의 최단 거리보다 짧을 때
                distances[n] = distance
                heapq.heappush(q, [distance, n]) # 다시 그 거리를 넣고 다른 노드를 탐색
					#마지막 컴퓨터가 감염되기까지 걸리는 시간이기 때문
    return distances

t = int(input())

for _ in range(t):
    n, d, c = tuple(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]

    for _ in range(d):
        a, b, s = tuple(map(int, input().split()))
        graph[b].append((a, s)) # 의존된 노드를 graph에 추가

    result = dijkstra(c, graph, n)
    count, seconds = 0, 0
 
    for target in result:
        if target == float('inf'):
            continue
        count += 1
        if seconds < target:
            seconds = target
    print(count, seconds)
