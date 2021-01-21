#!/usr/bin/env python3
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
n, t = list(map(int, input().split()))
a = list(map(int, input().split()))

data = defaultdict(list)
for i in range(len(a)):
    data[a[i]].append(i)

max_data = [a[-1]]
for i in reversed(range(1, n-1)):
    max_data.append(max(max_data[-1], a[i]))
max_data = list(reversed(max_data))

max_value = 0
for i in range(0, n-1):
    max_value = max(max_data[i]-a[i], max_value)

# print(max_value)


deleated = set()

ans = 0
for i in range(len(a)):
    num = a[i]

    if num+max_value in data:
        if num in deleated:
            continue
        if num+max_value in deleated:
            continue
        num_min = data[num]
        num_max = data[num+max_value]

        new_min = []
        new_max = []

        for j in num_max:
            if j > num_min[0]:
                new_max.append(j)
        for j in num_min:
            if j < num_max[-1]:
                new_min.append(j)
        # print(num, new_min, num+max_value, new_max)

        ans += max(len(new_max), len(new_min))
        deleated.add(num)
        deleated.add(num+max_value)

print(ans)
