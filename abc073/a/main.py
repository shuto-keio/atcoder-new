#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = set(list(str(input())))

if "9" in n:
    print("Yes")
else:
    print("No")
