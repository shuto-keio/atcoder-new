#!/usr/bin/env python3
from scipy.special import comb
from collections import Counter
import sys
sys.setrecursionlimit(10**6)

n, a, b = list(map(int, input().split()))
v = list(map(int, input().split()))

v.sort(reverse=True)

max_ = sum(v[:a])/a
c = Counter(v)

count_num = 0
for i in range(a):
    if v[i] == v[a-1]:
        count_num += 1

if v[0] == v[a-1]:
    ans = 0
    for i in range(a, min(c[v[a-1]], b)+1):
        ans += comb(c[v[a-1]], i, exact=True)
        # print(b, i)
else:
    ans = comb(c[v[a-1]], count_num, exact=True)

print(max_)
print(ans)
