#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

x = int(input())

count = 0
coor = 0
while(1):
    if coor >= x:
        break
    coor += (count+1)
    count += 1
print(count)
