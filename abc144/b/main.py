#!/usr/bin/env python3

n = int(input())

for b in range(1, 10):
    a = n//b

    if a*b == n:
        if a <= 9 and b <= 9:
            print("Yes")
            exit()
print("No")
