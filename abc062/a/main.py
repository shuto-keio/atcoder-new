#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

x, y = list(map(int, input().split()))

a = [1, 3, 5, 7, 8, 10, 12]
b = [4, 6, 9, 11]
c = [2]

if (x in a) and (y in a):
    print("Yes")
    exit()
if (x in b) and (y in b):
    print("Yes")
    exit()
if (x in b) and (y in c):
    print("Yes")
    exit()
print("No")
