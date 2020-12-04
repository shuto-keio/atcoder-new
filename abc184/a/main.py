#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))

print(a*d-b*c)
