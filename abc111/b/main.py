#!/usr/bin/env python3


n = int(input())

base = int("1"*len(str(n)))

for i in range(1, 10):
    if n <= base*i:
        print(base*i)
        exit()
