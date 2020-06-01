#!/usr/bin/env python3
import statistics

n = int(input())

a_list = []
b_list = []
for _ in range(n):
    a, b = list(map(int, input().split()))
    a_list.append(a)
    b_list.append(b)

a_median = statistics.median(a_list)
b_median = statistics.median(b_list)

# print(a_median)
# print(b_median)
if n % 2 != 0:
    print(int(b_median-a_median+1))
else:
    print(int(b_median*2-a_median*2+1))
