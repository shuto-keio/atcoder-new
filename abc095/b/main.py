#!/usr/bin/env python3

n, x = list(map(int, input().split()))
m = [int(input()) for i in range(n)]

ans = 0

ans += n
x -= sum(m)

ans += x//min(m)

print(ans)
