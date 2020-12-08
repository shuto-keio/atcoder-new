#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

h, w = list(map(int, input().split()))
s = [list(input()) for i in range(h)]

mod = 10**9+7

map_ = [[0]*(w+1) for i in range(h+1)]

right = [[0]*(w+1) for i in range(h+1)]
down = [[0]*(w+1) for i in range(h+1)]
diag = [[0]*(w+1) for i in range(h+1)]

for y in range(1, h+1):
    for x in range(1, w+1):
        if x == 1 and y == 1:
            now = 1
        elif s[y-1][x-1] == "#":
            continue
        else:
            now = (right[y][x-1] + down[y-1][x] + diag[y-1][x-1]) % mod
            # print(x, y, right[y][x-1], down[y-1][x], diag[y-1][x-1])
        map_[y][x] = (now) % mod
        right[y][x] = (right[y][x-1]+now) % mod
        down[y][x] = (down[y-1][x]+now) % mod
        diag[y][x] = (diag[y-1][x-1]+now) % mod

print((map_[-1][-1]) % mod)
