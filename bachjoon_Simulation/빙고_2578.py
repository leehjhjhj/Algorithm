from collections import deque

bingo = [list(map(int, input().split())) for _ in range(5)]
orders = [list(map(int, input().split())) for _ in range(5)]
result = [[False] * 5 for _ in range(5)]

def in_check(target):
    global result
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == target:
                result[i][j] = True


def bingo_check():
    bingo_cnt = 0
    for i in range(5):
        if result[i].count(True) == 5:
            bingo_cnt += 1

    for j in range(5):
        column = 0
        for k in range(5):
            if result[k][j] == True:
                column += 1
        if column == 5:
            bingo_cnt += 1

    x_set = deque([0, 1, 2, 3, 4])
    y_set = deque([0, 1, 2, 3, 4])
    down = 0
    for x, y in zip(x_set, y_set):
        if result[x][y] == True:
            down += 1
    if down == 5:
        bingo_cnt += 1

    up = 0
    for _ in range(5):
        x = x_set.popleft()
        y = y_set.pop()

        if result[x][y] == True:
            up += 1
    if up == 5:
        bingo_cnt += 1

    return bingo_cnt


def main():
    global result
    cnt = 0
    for i in range(5):
        for j in range(5):
            in_check(orders[i][j])
            cnt += 1
            if cnt >= 12:
                bingo_cnt = bingo_check()
                if  bingo_cnt >= 3:
                    return cnt

print(main())
