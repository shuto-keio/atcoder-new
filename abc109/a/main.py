#!/usr/bin/env python3

a, b = list(map(int, input().split()))

if (a*b) % 2 == 0:
    print("No")
else:
    print("Yes")
