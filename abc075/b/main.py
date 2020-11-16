#!/usr/bin/env python3
import numpy as np
import sys
sys.setrecursionlimit(10**6)


h, w = list(map(int, input().split()))
s = [list(str(input())) for i in range(h)]

s = np.array(s)

# print(s)

map_ = np.zeros((h, w), dtype=str)
for i in range(0, h):
    for j in range(0, w):
        if s[i][j] == "#":
            map_[i, j] = "#"
            continue
        start_y, end_y = max(i-1, 0), min(i+2, h)
        start_x, end_x = max(j-1, 0), min(j+2, w)
        tmp = np.sum(s[start_y:end_y, start_x:end_x] == "#")
        map_[i, j] = tmp
for i in range(len(map_)):
    print("".join(map_[i, :]))
