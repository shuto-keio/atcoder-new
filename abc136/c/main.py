#!/usr/bin/env python3

n = int(input())
h = list(map(int, input().split()))

h.reverse()


ans = 0
for i in range(1, len(h)):
    if h[i-1]-h[i] >= 0:
        continue
    elif h[i-1]-h[i] == -1:
        h[i] -= 1
    else:
        print("No")
        exit()

print("Yes")
