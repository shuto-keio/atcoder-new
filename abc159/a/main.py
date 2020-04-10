#!/usr/bin/env python3

n, m = map(int, input().split())

ans = n*(n-1)//2 + m*(m-1)//2
print(ans)
