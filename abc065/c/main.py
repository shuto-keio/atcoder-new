#!/usr/bin/env python3
# from math import factorial
import sys
sys.setrecursionlimit(10**6)


n, m = list(map(int, input().split()))
mod = 10**9+7

fact_list = [1]
for i in range(1, 10**5+1):
    fact_list.append(fact_list[-1]*i % mod)


def factorial(n):
    return fact_list[n]


if abs(n-m) >= 2:
    ans = 0

elif abs(n-m) == 1:
    # ans = n! * m!
    ans = factorial(n)*factorial(m)
else:
    # ans = n! * m!* 2
    ans = factorial(n)*factorial(m)*2

print(ans % mod)
