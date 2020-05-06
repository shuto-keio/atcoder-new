#!/usr/bin/env python3

n = int(input())
a = list(map(int, input().split()))

count = 1
ans_list = []
for i in range(n):
    if a[i] == count:
        count += 1
        ans_list.append(count)

if len(ans_list) == 0:
    print(-1)
else:
    print(n-len(ans_list))
