#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

a, b, x = list(map(int, input().split()))

if a % x != 0:
    a += (x - a % x)
b -= b % x

quo1 = a//x
quo2 = b//x
# print(a, b)
# print(quo1, quo2)
ans = quo2-quo1+1

print(ans)
