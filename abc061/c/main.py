#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n, k = list(map(int, input().split()))

data = [0]*(10**5)
for i in range(n):
    a, b = list(map(int, input().split()))
    data[a-1] += b

num = 0
for i in range(len(data)):
    num += data[i]
    if k <= num:
        print(i+1)
        exit()
