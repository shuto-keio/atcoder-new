#!/usr/bin/env python3

n = int(input())
w = [str(input()) for i in range(n)]

flag = 1

if len(w) != len(set(w)):
    flag = 0

# print(w)
moji = w[0][-1]
for i in w[1:]:
    # print(i)
    if moji != i[0]:
        flag = 0
    moji = i[-1]

if flag == 1:
    print("Yes")
else:
    print("No")
