#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = int(input())
mod = 10**9+7

n = 10**6


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


data = [0]*(n+1)


for i in range(1, n+1):
    tmp = prime_factorize(i)
    for j in tmp:
        data[j] += 1

ans = 1
for i in data:
    ans *= (i+1) % mod
    ans %= mod

print(ans)
