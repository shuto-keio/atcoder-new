#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n, T = list(map(int, input().split()))
t = list(map(int, input().split()))

ans = 0
for i in range(0, len(t)-1):
    if (t[i+1]-t[i]) <= T:
        ans_tmp = t[i+1]-t[i]
    else:
        ans_tmp = T
    ans += ans_tmp
    # print(ans_tmp)

ans += T
# print()
print(ans)
