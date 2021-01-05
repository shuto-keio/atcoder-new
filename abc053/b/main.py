#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

s = str(input())

index_a = 10**10
index_z = -1
for i in range(len(s)):
    if s[i] == "A":
        index_a = min(index_a, i)
    if s[i] == "Z":
        index_z = max(index_z, i)

print(index_z-index_a+1)
