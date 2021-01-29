#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))

sum_a = sum(a)
sum2_a = sum([i**2 for i in a])

ans = 10**10
for alpha in range(-100, 101):
    tmp = alpha**2*n-2*alpha*sum_a+sum2_a
    ans = min(ans, tmp)

print(ans)
