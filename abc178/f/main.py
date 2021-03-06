#!/usr/bin/env python3

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

idx_B = 0
ma = 0
for idx_A, a in enumerate(A):
    while idx_B < N and B[idx_B] < a:
        idx_B += 1
    # print(idx_A, idx_B)
    if ma < idx_A - idx_B:
        ma = idx_A-idx_B

Ans = (B+B)[N-ma-1:2*N-ma-1]

for a, b in zip(A, Ans):
    if a == b:
        print("No")
        exit()
print("Yes")
print(*Ans)
