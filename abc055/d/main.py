#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = int(input())
s = list(str(input()))

for ans_tmp in ["SS", "SW", "WS", "WW"]:

    for i in range(1, n-1):
        prepre = ans_tmp[-2]
        pre = ans_tmp[-1]
        flag = s[i]

        if pre == "S":
            if flag == "o":
                if prepre == "S":
                    now = "S"
                else:
                    now = "W"
            else:
                if prepre == "S":
                    now = "W"
                else:
                    now = "S"
        else:
            if flag == "o":
                if prepre == "S":
                    now = "W"
                else:
                    now = "S"
            else:
                if prepre == "S":
                    now = "S"
                else:
                    now = "W"
        ans_tmp += now
    flag = 1
    if ans_tmp[-1] == "S":
        if s[-1] == "o":
            if ans_tmp[0] == ans_tmp[-2]:
                pass
            else:
                flag = 0
        else:
            if ans_tmp[0] == ans_tmp[-2]:
                flag = 0
            else:
                pass
    else:
        if s[-1] == "o":
            if ans_tmp[0] == ans_tmp[-2]:
                flag = 0
            else:
                pass
        else:
            if ans_tmp[0] == ans_tmp[-2]:
                pass
            else:
                flag = 0
    if ans_tmp[0] == "S":
        if s[0] == "o":
            if ans_tmp[1] == ans_tmp[-1]:
                pass
            else:
                flag = 0
        else:
            if ans_tmp[1] == ans_tmp[-1]:
                flag = 0
            else:
                pass
    else:
        if s[0] == "o":
            if ans_tmp[1] == ans_tmp[-1]:
                flag = 0
            else:
                pass
        else:
            if ans_tmp[1] == ans_tmp[-1]:
                pass
            else:
                flag = 0

    if flag == 1:
        print(ans_tmp)
        exit()

print(-1)
