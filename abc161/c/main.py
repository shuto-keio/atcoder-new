#!/usr/bin/env python3

n, k = map(int, input().split())

if n > k:
    ans = n % k
else:
    ans = n
print(min(ans, k-ans))
