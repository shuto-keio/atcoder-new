#!/usr/bin/env python3

n = int(input())
s = list(str(input()))

num_list = []
r, g, b = 0, 0, 0
for i in range(n-1, -1, -1):
    if s[i] == "R":
        r += 1
    elif s[i] == "G":
        g += 1
    elif s[i] == "B":
        b += 1
    num_list.append([r, g, b])

num_list.reverse()

ans = 0
for i in range(n-2):
    if s[i] == "R":
        ans += num_list[i+1][1] * num_list[i+1][2]  # G , B
        for j in range(0, (n-i-1)//2):
            a, b, c = i, j+i+1, j+j+i+2
            # print(a, b, c)
            if {s[b], s[c]} == {"G", "B"}:
                ans -= 1
    if s[i] == "G":
        ans += num_list[i+1][0] * num_list[i+1][2]  # R, B
        for j in range(0, (n-i-1)//2):
            a, b, c = i, j+i+1, j+j+i+2
            # print(a, b, c)
            if {s[b], s[c]} == {"R", "B"}:
                ans -= 1
    if s[i] == "B":
        ans += num_list[i+1][0] * num_list[i+1][1]  # R, G
        for j in range(0, (n-i-1)//2):
            a, b, c = i, j+i+1, j+j+i+2
            # print(a, b, c)
            if {s[b], s[c]} == {"R", "G"}:
                ans -= 1
# print(num_list)
print(ans)
