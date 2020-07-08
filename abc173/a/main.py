#!/usr/bin/env python3
import math
n = int(input())

ans = math.ceil(n/1000)*1000
print(ans-n)
