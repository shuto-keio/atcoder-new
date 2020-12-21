#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

s = list(str(input()))

if len(set(s)) == len(s):
    print("yes")
else:
    print("no")
