#!/usr/bin/env python3

a, b, c, d = list(map(int, input().split()))

ans = [a*d, a*c, b*c, b*d]

print(max(ans))
