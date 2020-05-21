#!/usr/bin/env python3

s = list(str(input()))
k = int(input())

count = [[s[0], 1]]


for i in range(1, len(s)):
    if count[-1][0] == s[i]:
        count[-1][1] += 1
    else:
        count.append([s[i], 1])
# print(count)

ans = 0
if len(count) == 1:
    ans += (count[0][1]*k)//2

elif count[0][0] != count[-1][0]:
    for i in range(0, len(count)):
        letter, num = count[i]
        ans += (num//2)*k
else:
    for i in range(1, len(count)-1):
        letter, num = count[i]
        ans += (num//2)*k

    letter, num = count[0][0], count[0][1]+count[-1][1]
    ans += (num//2)*(k-1)

    ans += count[0][1]//2
    ans += count[-1][1]//2

print(ans)
