#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = str(input())

if n[0] == n[-1]:
    print("Yes")
else:
    print("No")
