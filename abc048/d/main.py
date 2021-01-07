#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

s = list(str(input()))

if s[0] == s[-1]:
    if len(s) % 2 == 0:
        print("First")
    else:
        print("Second")
else:
    if len(s) % 2 == 0:
        print("Second")
    else:
        print("First")
