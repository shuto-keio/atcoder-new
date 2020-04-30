#!/usr/bin/env python3

n = int(input())
A = list(map(int, input().split()))

flag = 0
for i in A:
    if i % 2 == 0:
        if i % 3 != 0 and i % 10 != 0:
            flag = 1
print("DENIED" if flag == 1 else "APPROVED")
