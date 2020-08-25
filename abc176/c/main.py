#!/usr/bin/env python3

n = int(input())
a = list(map(int, input().split()))

ans = 0
min_ = a[0]
for i in range(1, len(a)):
    if a[i] < min_:
        ans += min_-a[i]
    else:
        min_ = a[i]
print(ans)
