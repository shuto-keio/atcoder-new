#!/usr/bin/env python3

n, x = list(map(int, input().split()))
l = list(map(int, input().split()))

d = [0]
for i in range(n):
    d.append(d[-1]+l[i])

ans = [i <= x for i in d]
print(sum(ans))
