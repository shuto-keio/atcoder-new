#!/usr/bin/env python3

a, b, c = list(map(int, input().split()))

ans = (b//a)

print(min(ans, c))
