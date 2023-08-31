import heapq
import sys

input = sys.stdin.readline

def dijkstra(start, graph, n):
    distances = [float('inf')] * (n + 1)
    distances[start] = 0
    q = []
    heapq.heappush(q, [0, start])

    while q:
        curr_distance, curr_node = heapq.heappop(q)
        if distances[curr_node] < curr_distance:
            continue

        for n, n_time in graph[curr_node]:
            distance = curr_distance + n_time
            if distance < distances[n]:
                distances[n] = distance
                heapq.heappush(q, [distance, n])

    return distances

t = int(input())

for _ in range(t):
    n, d, c = tuple(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]

    for _ in range(d):
        a, b, s = tuple(map(int, input().split()))
        graph[b].append((a, s))

    result = dijkstra(c, graph, n)
    count, seconds = 0, 0
 
    for target in result:
        if target == float('inf'):
            continue
        count += 1
        if seconds < target:
            seconds = target
    print(count, seconds)
