#!/usr/bin/env python3

n = int(input())
b = list(map(int, input().split()))
a = list(map(int, input().split()))

ans = 0
for i in range(len(a)):
    power = a[i]
    if b[i] <= power:
        power = power - b[i]
        ans += b[i]
        b[i] = 0
        if b[i+1] <= power:
            power = power - b[i+1]
            ans += b[i+1]
            b[i+1] = 0
        else:
            ans += power
            b[i+1] -= power
            power = 0
    else:
        ans += power
        b[i] -= power
        power = 0
print(ans)
