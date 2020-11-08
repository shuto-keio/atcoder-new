#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = int(input())

if n % 2 == 0:
    print("White")
else:
    print("Black")
