#!/usr/bin/env python3

import math
a, b, n = list(map(int, input().split()))

if b-1 <= n:
    x = b-1
    ans = math.floor(a*x/b) - a * math.floor(x/b)
else:
    x = n
    ans = math.floor(a*x/b) - a * math.floor(x/b)
print(ans)
