#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

a, b, c = list(map(str, input().split()))

if b == "+":
    print(int(a) + int(c))
else:
    print(int(a) - int(c))
