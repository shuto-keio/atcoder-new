#!/usr/bin/env python3
from math import gcd
import sys
sys.setrecursionlimit(10**6)

n = int(input())
t = [int(input()) for i in range(n)]


def lcm(a, b):
    return a//gcd(a, b)*b


value = t[0]
for i in range(1, n):
    value = lcm(value, t[i])
print(value)
