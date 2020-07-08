#!/usr/bin/env python3

n, m, x, y = list(map(int, input().split()))
X = list(map(int, input().split()))
Y = list(map(int, input().split()))

x, y = min(x, y), max(x, y)

X, Y = max(X), min(Y)

x = max(X, x)
y = min(Y, y)

if x < y:
    print("No War")
else:
    print("War")
