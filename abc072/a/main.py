#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

X, t = list(map(int, input().split()))

print(max(0, X-t))
