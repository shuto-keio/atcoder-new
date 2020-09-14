#!/usr/bin/env python3
from math import factorial

n = int(input())
mod = 10**9+7

# if n == 1
# fac = [1]
# for i in range(2, n+2):
#     fac.append(fac[-1]*i % mod)

tens = [1]
for i in range(1, n+2):
    tens.append(tens[-1]*10 % mod)
nines = [1]
for i in range(1, n+2):
    nines.append(nines[-1]*9 % mod)
eights = [1]
for i in range(1, n+2):
    eights.append(eights[-1]*8 % mod)


# ans = 10**n - 8**n - (9**n-8**n)*2
ans = tens[n] - eights[n] - (nines[n]-eights[n])*2


print(ans % mod)
