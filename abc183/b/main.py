#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)


sx, sy, gx, gy = list(map(int, input().split()))

x = (gy*sx+sy*gx)/(sy+gy)

print(x)
