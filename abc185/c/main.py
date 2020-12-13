#!/usr/bin/env python3
import math
import sys
sys.setrecursionlimit(10**6)


def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


L = int(input())
base = comb(L-1, 11)
print(base)  # 10
