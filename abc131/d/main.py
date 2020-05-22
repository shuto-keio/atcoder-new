#!/usr/bin/env python3

n = int(input())
ab = [list(map(int, input().split())) for i in range(n)]


ab = sorted(ab, key=lambda x: x[1])

weight = 0
for w, d in ab:
    # print(weight, d)
    weight += w
    if weight > d:
        print("No")
        exit()
# print(weight, d)
print("Yes")
