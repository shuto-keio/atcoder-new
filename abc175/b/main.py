#!/usr/bin/env python3
import itertools
n = int(input())
l = list(map(int, input().split()))

ans = 0
for i in itertools.combinations(l, 3):
    i = sorted(list(i))
    # print(i)
    if i[0] == i[1] or i[1] == i[2]:
        continue
    if i[0]+i[1] > i[2]:
        # print(i)
        ans += 1

print(ans)
