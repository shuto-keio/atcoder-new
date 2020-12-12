#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = int(input())
a = [i-1 for i in list(map(int, input().split()))]

data = [0]*(10**5)
for i in a:
    if i-1 >= 0:
        data[i-1] += 1
    data[i] += 1
    if i+1 < n:
        data[i+1] += 1

print(max(data))
