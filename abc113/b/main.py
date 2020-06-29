#!/usr/bin/env python3

n = int(input())
t, a = list(map(int, input().split()))
h = list(map(int, input().split()))

h = [t-i*0.006 for i in h]


diff = 10**6
index = 0
for i, j in enumerate(h):
    if diff > abs(j-a):
        diff = abs(j-a)
        index = i+1
print(index)
