#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

s = list(str(input()))

s_compress = [s[0]]

for i in range(1, len(s)):
    if s_compress[-1] != s[i]:
        s_compress.append(s[i])
print(len(s_compress)-1)
