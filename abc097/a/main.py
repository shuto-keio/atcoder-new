#!/usr/bin/env python3

a, b, c, d = list(map(int, input().split()))

if abs(a-b) <= d and abs(b-c) <= d or abs(a-c) <= d:
    print("Yes")
else:
    print("No")
