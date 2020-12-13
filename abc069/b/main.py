#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

s = list(str(input()))

print(s[0]+str(len(s)-2)+s[-1])
