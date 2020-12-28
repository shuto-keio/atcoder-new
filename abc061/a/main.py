#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

a, b, c = list(map(int, input().split()))

if c >= a and c <= b:
    print('Yes')
else:
    print("No")
