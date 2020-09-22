#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

s = str(input())
obj_x, obj_y = list(map(int, input().split()))


x = []
y = []
flag = 0
num = 0
for i in range(len(s)):
    if s[i] == "T":
        if flag % 2 == 0:
            x.append(num)
        else:
            y.append(num)
        flag += 1
        num = 0
    else:
        num += 1

if num > 0:
    if flag % 2 == 0:
        x.append(num)
    else:
        y.append(num)


if x == []:
    x = [0]
if y == []:
    y = [0]


num_x = sum(x)
num_y = sum(y)

max_x = num_x*2+1
max_y = num_y*2+1

dp_x = [[0]*((len(x)+1)) for i in range(max_x)]
dp_y = [[0]*((len(y)+1)) for i in range(max_y)]

dp_x[num_x][0] = 1
dp_y[num_y][0] = 1

# print(x)
dp_x[num_x+x[0]][1] = 1

# print(dp_x)

for i in range(1, len(x)):
    num = x[i]
    for j in range(0, len(dp_x)):
        if j+num < max_x:
            dp_x[j+num][i+1] = max(dp_x[j+num][i+1], dp_x[j][i]*1)
        if j-num >= 0:
            dp_x[j-num][i+1] = max(dp_x[j-num][i+1], dp_x[j][i]*1)
        # if dp_x[j][i] == 1:
        #     print(j+num, j-num)
for i in range(0, len(y)):
    num = y[i]
    for j in range(0, len(dp_y)):
        if j+num < max_y:
            dp_y[j+num][i+1] = max(dp_y[j+num][i+1], dp_y[j][i]*1)
        if j-num >= 0:
            dp_y[j-num][i+1] = max(dp_y[j-num][i+1], dp_y[j][i]*1)
        # if dp_y[j][i] == 1:
        #     print(j+num, j-num)


if (num_x+obj_x) < len(dp_x) and (num_x+obj_x) >= 0:
    ans_x = dp_x[num_x+obj_x][-1]
else:
    print("No")
    exit()
if (num_y+obj_y) < len(dp_y) and (num_y+obj_y) >= 0:
    ans_y = dp_y[num_y+obj_y][-1]
else:
    print("No")
    exit()

# print(dp_x)
if ans_x*ans_y == 1:
    print("Yes")
else:
    print("No")
