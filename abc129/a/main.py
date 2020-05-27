#!/usr/bin/env python3

p, q, r = list(map(int, input().split()))

print(min(p+q, q+r, r+p))
