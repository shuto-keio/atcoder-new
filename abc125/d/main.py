#!/usr/bin/env python3

n = int(input())
a = list(map(int, input().split()))

num_minus = 0
for i in range(n):
    if a[i] < 0:
        num_minus += 1

a_plus = [abs(i) for i in a]

# print(num_minus)
# print(a_plus)
if num_minus % 2 == 0:
    print(sum(a_plus))
else:
    print(sum(a_plus)-2*min(a_plus))
