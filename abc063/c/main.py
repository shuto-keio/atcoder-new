#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = int(input())
s = [int(input()) for i in range(n)]

multi_ten = []
multi_other = []
ans = 0

for i in s:
    ans += i
    if i % 10 == 0:
        multi_ten.append(i)
    else:
        multi_other.append(i)
multi_other.sort()

if ans % 10 != 0:
    print(ans)
else:
    if len(multi_other) > 0:
        print(ans-multi_other[0])
    else:
        print(0)
