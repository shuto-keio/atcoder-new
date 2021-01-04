#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

w, a, b = list(map(int, input().split()))

if b <= a+w and b >= a:
    print(0)
else:
    # print(abs(b-a-w), abs(b+w-a))
    print(min(abs(b-a-w), abs(b+w-a)))
