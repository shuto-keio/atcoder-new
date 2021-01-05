#!/usr/bin/env python3
# import deque
from collections import Counter
import sys
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))

c = Counter(a)

ans = n
for key, value in c.items():
    if value >= 2:
        ans -= (value-1)
if ans % 2 == 1:
    print(ans)
else:
    print(ans-1)
