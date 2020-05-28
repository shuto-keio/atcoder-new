#!/usr/bin/env python3

n = int(input())

data = {}
for i in range(n):
    s, p = list(map(str, input().split()))
    p = int(p)
    if s in data:
        data[s].append([p, i+1])
    else:
        data[s] = [[p, i+1]]

# print(data)
name_list = list(data.keys())
name_list.sort()


for i in name_list:
    data_tmp = data[i]
    data_tmp = sorted(data_tmp, key=lambda x: x[0], reverse=True)
    for j in data_tmp:
        print(j[1])
