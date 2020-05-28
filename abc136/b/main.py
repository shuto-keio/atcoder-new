#!/usr/bin/env python3

n = int(input())

ans = 0
for i in range((len(str(n))+1)//2):
    num = 10**(2*i)
    line = num*10-1
    # print(num)
    # print(line)
    # print()

    if n-line >= 0:
        ans += num*9
    else:
        ans += n-num+1

print(ans)
# n-num
# 9, 900
# if
# 1, 100, 10000
