#!/usr/bin/env python3

from math import factorial

n, k = list(map(int, input().split()))

blue = k
red = n-k

mod = 10**9 + 7

fac_list = [1]

for i in range(1, 2001):
    fac_list.append(fac_list[-1]*i)


def comb(a, b):
    ans = fac_list[a]//(fac_list[b]*fac_list[a-b])
    return ans % mod


for i in range(1, k+1):
    gap = red+1

    ans = comb(gap, i) * comb(blue-1, i-1)
    print(ans % mod)

# (n-k+1)!/(n-k)!

# (n-k+2)!/(n-k)!-(n-k+1)!/(n-k)!
