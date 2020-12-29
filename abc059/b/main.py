#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

a = int(input())
b = int(input())

if a > b:
    print("GREATER")
elif a == b:
    print("EQUAL")
else:
    print("LESS")
