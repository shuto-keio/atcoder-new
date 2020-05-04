#!/usr/bin/env python3

k = int(input())
a, b = list(map(int, input().split()))

if (b//k)*k >= a:
    print("OK")
else:
    print("NG")
