#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

a, b, c = list(map(int, input().split()))

if a == b:
    print(c)
elif a == c:
    print(b)
else:
    print(a)
