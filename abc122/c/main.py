#!/usr/bin/env python3

n, q = list(map(int, input().split()))
s = list(str(input()))


count = [0]


for i in range(1, len(s)):
    if s[i-1]+s[i] == "AC":
        count.append(count[i-1]+1)
    else:
        count.append(count[i-1])

# print(count)

for _ in range(q):
    l, r = list(map(int, input().split()))
    print(count[r-1]-count[l-1])
