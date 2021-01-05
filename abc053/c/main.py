#!/usr/bin/env python3
import math
import sys
sys.setrecursionlimit(10**6)

x = int(input())

ans = math.ceil(x/(11))

if ans*11-5 >= x:
    print(ans*2-1)
else:
    print(ans*2)
