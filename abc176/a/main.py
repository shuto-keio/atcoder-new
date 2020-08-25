#!/usr/bin/env python3
import math

n, x, t = list(map(int, input().split()))

print(math.ceil(n/x)*t)
