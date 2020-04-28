#!/usr/bin/env python3

n, k = list(map(int, input().split()))

mod = 10**9+7

ans = 0
for k_ in range(k, n+2):
    low_lim = (0+(k_-1))*k_//2
    up_lim = ((n-k_+1)+n)*k_//2
    ans += up_lim - low_lim + 1

print(ans % mod)
