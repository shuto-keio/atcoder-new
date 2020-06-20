#!/usr/bin/env python3

n = int(input())
a = list(map(int, input().split()))

max_a = max(a)
c = {a_tmp: 0 for a_tmp in a}
for a_tmp in a:
    c[a_tmp] += 1

d = {a_tmp: 0 for a_tmp in a}
for a_tmp in a:
    if c[a_tmp] > 0:
        t = 2
        while a_tmp*t <= max_a:
            d[a_tmp*t] = 1
            t += 1
ans = 0
for a_tmp in a:
    if c[a_tmp] == 1 and d[a_tmp] == 0:
        ans += 1

print(ans)
