#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n, m = list(map(int, input().split()))
a = [str(input()) for i in range(n)]
b = [str(input()) for i in range(m)]

for i in range(0, n-m+1):
    for j in range(0, n-m+1):
        flag = 0
        for x in range(m):
            for y in range(m):
                # print(i, j, x, y)
                if a[i+x][j+y] == b[x][y]:
                    # print("match")
                    pass
                else:
                    flag = 1
                    break
            if flag == 1:
                break
        if flag == 0:
            print("Yes")
            exit()
print("No")
