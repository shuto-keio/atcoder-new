#!/usr/bin/env python3

t = list(str(input()))

t_new = []
for i in t:
    if i == "?":
        t_new.append("D")
    else:
        t_new.append(i)

for i in t_new:
    print(i, end="")
# ans = 0
# for i in range(n):
#     if t_new[i] == D:
#         ans += 1

# for i in range(1, n):
#     if t_new[i-1] == P and t_new[i] == D:
#         ans += 1
# print(ans)
