#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = int(input())

if n == 1:
    print("Hello World")
else:
    ans = 0
    ans += int(input())
    ans += int(input())
    print(ans)
