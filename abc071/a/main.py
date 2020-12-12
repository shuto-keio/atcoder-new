#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

x, a, b = list(map(int, input().split()))

if abs(x-a) > abs(x-b):
    print("B")
else:
    print("A")
