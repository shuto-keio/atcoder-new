#!/usr/bin/env python3
from collections import deque
import sys
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))

b = deque([])

flag = 0
for i in a:
    if flag == 0:
        b.append(i)
        flag = 1
    else:
        b.appendleft(i)
        flag = 0

if flag == 0:
    print(*b)
else:
    print(*reversed(b))
