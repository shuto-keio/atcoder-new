#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

w, h, n = list(map(int, input().split()))

x_min = 0
x_max = w
y_min = 0
y_max = h
for i in range(n):
    x, y, a = list(map(int, input().split()))
    if a == 1:
        x_min = max(x_min, x)
    elif a == 2:
        x_max = min(x_max, x)
    elif a == 3:
        y_min = max(y_min, y)
    elif a == 4:
        y_max = min(y_max, y)

if (x_max-x_min) < 0 or (y_max-y_min) < 0:
    print(0)
    exit()

print(max(0, (x_max-x_min)*(y_max-y_min)))
