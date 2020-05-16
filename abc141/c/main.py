#!/usr/bin/env python3

n, k, q = list(map(int, input().split()))

score = [k for _ in range(n)]

count = [0 for _ in range(n)]
for i in range(q):
    a = int(input())
    count[a-1] += 1

for i in range(n):
    score = k+count[i]-q
    if score >= 1:
        print("Yes")
    else:
        print("No")
