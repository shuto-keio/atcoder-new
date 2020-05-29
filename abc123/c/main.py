#!/usr/bin/env python3

n, a, b, c, d, e = [int(input()) for _ in range(6)]


ans = (n-1)//min(a, b, c, d, e)+1 + 4
print(ans)
