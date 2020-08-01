#!/usr/bin/env python3

n, k = list(map(int, input().split()))

if n % k != 0:
    print(1)
else:
    print(0)
