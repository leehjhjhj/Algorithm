from collections import deque

def one(arr, x):
    if arr[x] == 1:
        return arr
    else:
        arr[x] = 1
        return arr
def two(arr, x):
    if arr[x] == 0:
        return arr
    else:
        arr[x] = 0
        return arr

def thr(arr):
    arr = deque(arr)
    arr.rotate(1)
    if arr[0] == 1:
        arr[0] = 0
    return list(arr)

def four(arr):
    arr = deque(arr)
    arr.rotate(-1)
    if arr[-1] == 1:
        arr[-1] = 0
    return list(arr)

n, m = map(int, input().split())
train = [[0] * 20 for _ in range(n)]
order = [
    list(map(int,input().split()))
    for _ in range(m)
]
box =[]
cnt = 0

for i in range(m):
    if order[i][0] == 1:
        train[order[i][1] -1] = one(train[order[i][1] -1], order[i][2] -1)
    elif order[i][0] == 2:
        train[order[i][1] -1] = two(train[order[i][1] -1], order[i][2] -1)
    elif order[i][0] == 3:
        train[order[i][1] -1] = thr(train[order[i][1] -1])
    elif order[i][0] == 4:
        train[order[i][1] -1] = four(train[order[i][1] -1])


for target in train:
    if target in box:
        continue
    else:
        box.append(target)
        cnt += 1
print(cnt)
    