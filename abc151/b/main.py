#!/usr/bin/env python3

n, k, m = list(map(int, input().split()))
a = list(map(int, input().split()))

ans = m*n-sum(a)

if ans > k:
    print(-1)
elif ans <= 0:
    print(0)
else:
    print(ans)
