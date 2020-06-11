#!/usr/bin/env python3

n = int(input())
h = list(map(int, input().split()))


ans = 0
for num in reversed(range(1, max(h)+1)):
    # print("num", num)
    # print(h)
    count = 0
    for j in range(0, n-1):
        if h[j] == num and h[j+1] < num:
            count += 1
        if h[j] == num:
            h[j] = num-1
    if h[-1] == num:
        count += 1
        h[-1] = num-1
    ans += count

print(ans)
