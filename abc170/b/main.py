#!/usr/bin/env python3

x, y = list(map(int, input().split()))

# a+b = x
# 2*a+4*b = y

a = (4*x-y)//2
b = (y-2*x)//2


if a < 0 or b < 0:
    print("No")
    exit()
if a == 0 and b == 0:
    print("No")
    exit()
if a+b != x or 2*a+4*b != y:
    print("No")
    exit()

print("Yes")
