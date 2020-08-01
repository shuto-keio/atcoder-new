#!/usr/bin/env python3

n = int(input())

a = 0

while(1):
    tmp = n - 7*a
    if tmp % 4 == 0:
        print("Yes")
        exit()
    a += 1
    if a*7 > n:
        print("No")
        exit()
