#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

a, b, c = list(map(int, input().split()))

data = set()
i = 1
while(1):
    tmp = a*i % b
    if tmp in data:
        break
    else:
        data.add(tmp)
    i += 1

# print(data)
if c in data:
    print("YES")
else:
    print("NO")
