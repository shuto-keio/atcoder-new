#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

a, b, c = list(map(int, input().split()))

if (a+b == c) or (a+c == b) or (b+c == a):
    print("Yes")
else:
    print("No")
