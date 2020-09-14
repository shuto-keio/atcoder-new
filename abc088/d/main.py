#!/usr/bin/env python3
from collections import deque

h, w = list(map(int, input().split()))
s = [list(str(input())) for i in range(h)]

map_ = [[10**9]*w for i in range(h)]
# map_[0][0] = 10*

num_black = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            num_black += 1


dq = deque([[0, 0, 1]])


ans = 0
while(len(dq) > 0):
    y, x, dis = dq.popleft()

    if map_[y][x] > dis:
        map_[y][x] = dis
    else:
        continue

    for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if y+i < 0 or y+i >= h:
            continue
        if x+j < 0 or x+j >= w:
            continue
        if map_[y+i][x+j] <= dis:
            continue
        if s[y+i][x+j] == "#":
            continue
        else:
            dq.appendleft([y+i, x+j, dis+1])

ans = map_[-1][-1]
# print(map_)

if ans == 10**9:
    print(-1)
else:
    print(w*h-ans-num_black)
