from collections import deque

target = deque(input())

def is_pelin(target):
    while len(target) > 1:
        if target.popleft() != target.pop():
            return 0
    return 1

print(is_pelin(target))