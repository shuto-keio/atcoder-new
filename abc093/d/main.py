#!/usr/bin/env python3

q = int(input())
ab = [list(map(int, input().split())) for i in range(q)]

for a, b in ab:
    if a == b:
        print((a-1)*2)
        continue

    value = int((a*b)**0.5)

    if value**2 == a*b:
        ans = value*2-3
        # print(value, ans, 1)
    elif value*(value+1) >= a*b:
        ans = value*2-2
        # print(value, ans, 2)
    else:
        ans = value*2-1
        # print(value, ans, 3)
    print(ans)
