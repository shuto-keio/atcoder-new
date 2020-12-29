#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

a, b, c = list(map(str, input().split()))

if a[-1] == b[0] and b[-1] == c[0]:
    print("YES")
else:
    print("NO")
