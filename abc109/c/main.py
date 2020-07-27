#!/usr/bin/env python3
import math

n, x = list(map(int, input().split()))
x_list = list(map(int, input().split())) + [x]

x_list.sort()

x_diff = [x_list[i+1]-x_list[i] for i in range(len(x_list)-1)]

# print(x_diff)
A = x_diff

value = A[0]
for i in range(1, len(A)):
    value = math.gcd(value, A[i])
print(value)
