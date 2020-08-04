#!/usr/bin/env python3

a = list(map(int, input().split()))

a.sort(reverse=True)

ans = 0
for i in range(1, len(a)):
    ans += a[i-1]-a[i]
print(ans)
