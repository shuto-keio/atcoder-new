#!/usr/bin/env python3
from collections import deque

n = int(input())
a = list(map(int, input().split()))

if n == 2:
    print(max(a))
    exit()

a.sort(reverse=True)

d = deque([a[1]]*2)

ans = a[0]
for i in a[2:]:
    d.append(i)
    d.append(i)
    ans += d.popleft()

print(ans)
