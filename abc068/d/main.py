#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

k = int(input())

quo = k//50
rem = k % 50

ans = [49+quo]*50

for i in range(rem):
    ans[i] += 50 - (rem-1)

for i in range(50-rem):
    ans[-i-1] -= rem

print(50)
print(*ans)
