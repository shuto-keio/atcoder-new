#!/usr/bin/env python3

n = str(input())

ans = 0
count = 1
for i in reversed(n):
    ans += int(i)
    ans = ans % 9
    count *= 10
if ans == 0:
    print("Yes")
else:
    print("No")
