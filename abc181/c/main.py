#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = int(input())
xy = []
for i in range(n):
    x, y = list(map(int, input().split()))
    xy.append((x, y))

flag = 0
for i in range(len(xy)):
    for j in range(len(xy)):
        if xy[i] == xy[j]:
            continue

        for k in range(len(xy)):
            if xy[i] == xy[k] or xy[j] == xy[k]:
                continue
            x1, y1 = xy[i]
            x2, y2 = xy[j]
            x3, y3 = xy[k]

            # slope1 = (y1-y2)/(x1-x2)
            # slope2 = (y2-y3)/(x2-x3)

            if (y1-y2)*(x2-x3) == (y2-y3)*(x1-x2):
                flag = 1
                break
        if flag == 1:
            break
    if flag == 1:
        break

if flag == 1:
    print("Yes")
else:
    print("No")
