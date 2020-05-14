#!/usr/bin/env python3

a = list(map(int, input().split()))

if sum(a) >= 22:
    print("bust")
else:
    print("win")
