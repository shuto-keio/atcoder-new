#!/usr/bin/env python3
x, n = list(map(int, input().split()))
p = list(map(int, input().split()))

p_list = [0]*100

for i in p:
    p_list[i-1] = 1

p_list = [0]+p_list+[0]

dis = 100
index = -1
for i, j in enumerate(p_list):
    if j == 1:
        continue
    # print(i+1, abs(x-(i+1)))
    if dis > abs(x-i):
        dis = abs(x-i)
        index = i
        # index=i

print(index)
