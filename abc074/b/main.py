#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = int(input())
k = int(input())
x = list(map(int, input().split()))

ans = 0
for i in x:
    ans1 = i*2
    ans2 = (k-i)*2

    if ans2 >= 0:
        ans += min(ans1, ans2)
    else:
        ans += ans1
print(ans)
