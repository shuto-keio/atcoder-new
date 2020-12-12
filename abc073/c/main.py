#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = int(input())

ans = set([])

for i in range(n):
    a = int(input())

    if a in ans:
        ans.remove(a)
    else:
        ans.add(a)
print(len(ans))
