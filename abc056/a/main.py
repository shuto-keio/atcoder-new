#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

a, b = list(map(str, input().split()))

if a == "H" and b == "H":
    print("H")
elif a == "H" and b == "D":
    print("D")
elif a == "D" and b == "H":
    print("D")
elif a == "D" and b == "D":
    print("H")
