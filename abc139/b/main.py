#!/usr/bin/env python3
import math

a, b = list(map(int, input().split()))

ans = (b-1)/(a-1)

print(math.ceil(ans))
