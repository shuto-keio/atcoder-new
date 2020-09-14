#!/usr/bin/env python3
from math import factorial

mod = 10**9+7
s = int(input())

keta = s//3
amari = s % 3

ans = 0
for now_keta in reversed(range(1, keta+1)):
    ans_tmp = factorial(
        amari+now_keta-1)//(factorial(now_keta - 1)*factorial(amari)) % mod
    amari += 3
    ans += ans_tmp

print(ans % mod)
