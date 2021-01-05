#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n, m = list(map(int, input().split()))

num = (2*n+m)//4

print(min(num, m//2))
