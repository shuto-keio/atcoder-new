#!/usr/bin/env python3

k, x = list(map(int, input().split()))

if 500*k >= x:
    print("Yes")
else:
    print("No")
