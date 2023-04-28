def solution(n, computers):
    answer = 0
    relation = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                relation[i + 1].append(j + 1)
                relation[j + 1].append(i + 1)
                
    def dfs(i):
        for v in relation[i]:
            if visited[v] == 0:
                visited[v] = 1
                dfs(v)
                
    for i in range(1, n + 1):
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)
            answer += 1
    
    return answer
