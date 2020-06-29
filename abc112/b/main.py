#!/usr/bin/env python3

n, t = list(map(int, input().split()))

ct = [list(map(int, input().split())) for _ in range(n)]

ct = sorted(ct, key=lambda x: x[0])

# print(n, t)
# print(ct)
for i in ct:
    if i[1] <= t:
        print(i[0])
        exit()

print("TLE")
