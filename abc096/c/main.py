#!/usr/bin/env python3

h, w = list(map(int, input().split()))
s = [list(str(input())) for i in range(h)]

for i in range(h):
    for j in range(w):
        tmp = 1
        if s[i][j] == "#":
            tmp = 0
            if i > 0:
                if s[i-1][j] == "#":
                    tmp += 1
            if i < h-1:
                if s[i+1][j] == "#":
                    tmp += 1
            if j > 0:
                if s[i][j-1] == "#":
                    tmp += 1
            if j < w-1:
                if s[i][j+1] == "#":
                    tmp += 1
        if tmp == 0:
            print("No")
            exit()
print("Yes")
