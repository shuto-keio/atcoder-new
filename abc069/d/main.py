#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

h, w = list(map(int, input().split()))
n = int(input())
a = list(map(int, input().split()))

ans = [[-1]*w for i in range(h)]

x, y = 0, 0
flag = 0
for color, num in enumerate(a):
    for i in range(num):
        ans[y][x] = color+1
        if flag == 0:
            x += 1
        else:
            x -= 1

        if x == w:
            x = w-1
            y += 1
            flag = 1
        if x == -1:
            x = 0
            y += 1
            flag = 0

for i in ans:
    print(*i)
