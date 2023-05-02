OFFSET = 1000
MAX_R = 2000
checked = [[0] * (MAX_R + 1) for _ in range(MAX_R + 1)]
for i in range(1, 3):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1 + OFFSET, x2 + OFFSET):
        for k in range(y1 + OFFSET, y2 + OFFSET):
            checked[j][k] += i


min_x, max_x = MAX_R, -MAX_R
min_y, max_y = MAX_R, -MAX_R
is_one = False

for i in range(MAX_R + 1):
    for j in range(MAX_R + 1):

        if checked[i][j] == 1:
            is_one = True
            min_x = min(min_x, i)
            max_x = max(max_x, i)
            min_y = min(min_y, j)
            max_y = max(max_y, j)
        
if not is_one:
    print(0)
else:
    print((max_x + 1 - min_x) * (max_y + 1 - min_y))
            
