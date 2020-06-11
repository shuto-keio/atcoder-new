#!/usr/bin/env python3


n = int(input())
L = list(map(int, input().split()))

if (sum(L)-max(L))-max(L) > 0:
    print("Yes")
else:
    print("No")
