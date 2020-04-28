#!/usr/bin/env python3

n = int(input())
a = list(map(int, input().split()))

subordinate_list = [0 for _ in range(n)]

for i in range(len(a)):
    subordinate_list[a[i]-1] += 1

for i in range(n):
    print(subordinate_list[i])
