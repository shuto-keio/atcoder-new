#!/usr/bin/env python3

n = int(input())
a = list(map(int, input().split()))

order = []
for i in range(n):
    order.append([i, a[i]])

order = sorted(order, key=lambda a: a[1])

for i in range(len(order)):
    print("{} ".format(order[i][0]+1), end="")
print()
