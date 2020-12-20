#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

r, g, b = list(map(int, input().split()))

num = int(str(r)+str(g)+str(b))

if num % 4 == 0:
    print("YES")
else:
    print("NO")
