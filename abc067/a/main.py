#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

a, b = list(map(int, input().split()))

if a % 3 == 0 or b % 3 == 0 or (a+b) % 3 == 0:
    print("Possible")
else:
    print("Impossible")
