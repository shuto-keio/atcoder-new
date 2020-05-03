#!/usr/bin/env python3


n, k = list(map(int, input().split()))

list_sunuke = []

for i in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    list_sunuke += a

print(n-len(set(list_sunuke)))
