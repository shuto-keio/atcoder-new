#!/usr/bin/env python3

a = int(input())
p = [int(input()) for _ in range(a)]

print(sum(p)-max(p)+max(p)//2)
