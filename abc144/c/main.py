#!/usr/bin/env python3

n = int(input())

count = 1
ans = 10**12
while(count <= (n)**0.5):
    if n % count == 0:
        ans_tmp = (count-1) + (n//count-1)
    ans = min(ans, ans_tmp)
    count += 1

print(ans)
