#!/usr/bin/env python3

n = int(input())
a = list(map(int, input().split()))


ans = 1
flag = 0
for i in a:
    ans *= i
    if ans > 10**18:
        flag = 1
        ans = 0
    if i == 0:
        print(0)
        exit()
if flag == 1:
    print(-1)
else:
    print(ans)
