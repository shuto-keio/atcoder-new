#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

a, b, c, d = list(map(int, input().split()))

print(max(a*b, c*d))
