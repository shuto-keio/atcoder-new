#!/usr/bin/env python3

n, m = list(map(int, input().split()))

flag = [0 for _ in range(n)]
wa_num_list = [0 for _ in range(n)]

for i in range(m):
    p, s = list(map(str, input().split()))
    p = int(p)
    if flag[p-1] == 0:
        if s == "WA":
            wa_num_list[p-1] += 1
        else:
            flag[p-1] = 1

pen = 0
for i in range(n):
    if flag[i] == 1:
        pen += wa_num_list[i]

print(sum(flag), pen)
