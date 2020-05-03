#!/usr/bin/env python3
import numpy as np

n = int(input())
a = list(map(int, input().split()))


x = np.array(a[1:])-a[0]+np.arange(1, n)
# print(x)

y = np.array(a[1:])+a[0]-np.arange(0, n-1)
# print(y)

count = {}
ans = 0
for i in range(0, n-1):
    if not x[i] in count:
        count[x[i]] = 1
    else:
        count[x[i]] += 1

    if y[i] == 1:
        ans += 1
    if -y[i]+1 in count:
        ans += count[-y[i]+1]
# print(count)
print(ans)
