n = int(input())
OFFSET = 100
MAX_R = 200
grid = [[0] * (MAX_R + 1) for _ in range(MAX_R + 1)]

ans = 0
for _ in range(n):
    x1, y1, x2, y2 = map(int,input().split())

    for i in range(x1 + OFFSET, x2 + OFFSET):
        for j in range(y1, y2):
            if grid[i][j] != 1:
                grid[i][j] = 1

for i in range(201):
    for j in range(201):
        if grid[i][j] == 1:
            ans += 1
print(ans)
