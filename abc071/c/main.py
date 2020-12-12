#!/usr/bin/env python3
from collections import Counter
import sys
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))

c = Counter(a)

over_4 = []
over_2 = []

for key, value in c.items():
    if value >= 4:
        over_4.append(key)
    if value >= 2:
        over_2.append(key)
over_2.sort(reverse=True)

if len(over_4) >= 1:
    ans1 = max(over_4)**2
else:
    ans1 = 0

if len(over_2) >= 2:
    ans2 = over_2[0]*over_2[1]
else:
    ans2 = 0

print(max(ans1, ans2))
