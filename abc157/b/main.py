#!/usr/bin/env python3

A = [list(map(int, input().split())) for i in range(3)]

B = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
N = int(input())

# print(A)
for i in range(N):
    num = int(input())
    for j in range(3):
        for k in range(3):
            if A[j][k] == num:
                B[j][k] = 1

# print(B)
flag = 0
for i in range(3):
    if B[0][i] == 1 and B[1][i] == 1 and B[2][i] == 1:
        flag = 1

for i in range(3):
    if B[i][0] == 1 and B[i][1] == 1 and B[i][2] == 1:
        flag = 1

if B[0][0] == 1 and B[1][1] == 1 and B[2][2] == 1:
    flag = 1

if B[0][2] == 1 and B[1][1] == 1 and B[2][0] == 1:
    flag = 1

if flag == 0:
    print("No")
else:
    print("Yes")
