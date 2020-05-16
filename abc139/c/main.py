#!/usr/bin/env python3

n = int(input())
h = list(map(int, input().split()))

ans = 0
count = 0
for i in range(1, n):
    # print(h)
    # print(h[i-1], h[i])
    if h[i-1] >= h[i]:
        count += 1
    else:
        ans = max(count, ans)
        count = 0
    # print(count)
ans = max(count, ans)
print(ans)
