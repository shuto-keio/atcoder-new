#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

mod = 1000000007

n = int(input())
s1 = list(str(input()))
s2 = list(str(input()))


if s1[0] == s2[0]:
    ans = 3
    index = 1
    onetype_old = True
else:
    ans = 6
    index = 2
    onetype_old = False

while(index < n):
    onetype_now = (s1[index] == s2[index])

    if onetype_old:
        if onetype_now:
            ans *= 2
            ans %= mod
        else:
            ans *= 2
            ans %= mod
    else:
        if onetype_now:
            ans *= 1
        else:
            ans *= 3
            ans %= mod
    if onetype_now:
        index += 1
    else:
        index += 2
    onetype_old = onetype_now

print(ans)
