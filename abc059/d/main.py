#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

x, y = list(map(int, input().split()))

if abs(x-y) <= 1:
    print("Brown")
else:
    print("Alice")
