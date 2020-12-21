#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

a, b = list(map(int, input().split()))

if a+b < 10:
    print(a+b)
else:
    print("error")
