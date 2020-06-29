#!/usr/bin/env python3

n, m = list(map(int, input().split()))

py = []
city = {i+1: [] for i in range(n)}
for i in range(m):
    p, y = list(map(int, input().split()))
    city[p].append(y)
    py.append([p, y])


for i in city.values():
    i.sort()
# print(city)

ans = {i+1: {} for i in range(n)}
for key, value in city.items():
    for i in range(len(value)):
        ans[key][value[i]] = i+1

for p, y in py:
    # print(p, ans[p][y])
    print("{:06}{:06}".format(p, ans[p][y]))
