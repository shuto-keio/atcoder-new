#!/usr/bin/env python3

n = int(input())
p = list(map(int, input().split()))

count = 0
for i in range(len(p)):
    if p[i] != i+1:
        count += 1
if count >= 3:
    print("NO")
else:
    print("YES")
