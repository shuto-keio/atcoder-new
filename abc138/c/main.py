#!/usr/bin/env python3

n = int(input())
v = list(map(int, input().split()))


v.sort()
ans = v[0]

for i in v[1:]:
    ans = (ans+i)/2
print(ans)
