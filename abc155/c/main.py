#!/usr/bin/env python3

n = int(input())

string_dict = {}

for i in range(n):
    s = str(input())
    if s in string_dict.keys():
        string_dict[s] += 1
    else:
        string_dict[s] = 1

ans = []
ans_value = 0
for key, value in string_dict.items():
    if ans_value < value:
        ans = [key]
        ans_value = value
    elif ans_value == value:
        ans.append(key)

ans.sort()

for i in ans:
    print(i)
