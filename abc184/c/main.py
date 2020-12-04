#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))

if a == c and b == d:
    print(0)
    exit()

if a+b == c+d or a-b == c-d or abs(a-c)+abs(b-d) <= 3:
    print(1)
    exit()

if (a+b+c+d) % 2 == 0:
    print(2)
    exit()
if abs(a-c)+abs(b-d) <= 6:
    print(2)
    exit()
if abs((a+b)-(c+d)) <= 3:
    print(2)
    exit()
if abs((a-b)-(c-d)) <= 3:
    print(2)
    exit()


print(3)
