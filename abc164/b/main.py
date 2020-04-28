#!/usr/bin/env python3
import math

a, b, c, d = list(map(int, input().split()))

if math.ceil(a/d) >= math.ceil(c/b):
    print("Yes")
else:
    print("No")
