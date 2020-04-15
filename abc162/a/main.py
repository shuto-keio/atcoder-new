#!/usr/bin/env python3

n = int(input())

n = list(str(n))

flag = 0

for i in n:
    if i == str(7):
        flag = 1

print("Yes" if flag == 1 else "No")
