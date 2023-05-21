import sys
from collections import deque

words= []

searching_set = set(["(", ")", "[", "]"])

while True:
    word = input()
    if word == ".":
        break

    rst = deque()
    for target in word:
        if target in searching_set:
            rst.append(target)
            if len(rst) >= 2 and ((rst[-2] == "(" and rst[-1] == ")") or (rst[-2] == "[" and rst[-1] == "]")):
               for _ in range(2):
                   rst.pop()
    if not rst:
        print("yes")
    else:
        print("no")