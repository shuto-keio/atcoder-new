#!/usr/bin/env python3
s = str(input())

mod = 2019

div_memo = [0 for _ in range(mod)]

num = 0
d = 1
for n in reversed(s):
    num += int(n)*d
    num %= 2019
    div_memo[num] += 1
    d *= 10
    d %= 2019

ans = 0
for i in range(len(div_memo)):
    ans += div_memo[i]*(div_memo[i]-1)//2

ans += div_memo[0]
print(int(ans))
