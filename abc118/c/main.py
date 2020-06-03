#!/usr/bin/env python3

import fractions
n = int(input())
a = list(map(int, input().split()))


value = a[0]
for i in range(1, n):
    value = fractions.gcd(value, a[i])
print(value)

