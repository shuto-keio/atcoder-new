#!/usr/bin/env python3

s = list(str(input()))

ans = [0 for _ in range(len(s))]

num_r = 0
num_l = 0
for i in range(len(s)-1):
    # print(s[i])
    if s[i] == "R":
        num_r += 1
    else:
        num_l += 1

    if s[i] == "R" and s[i+1] == "L":
        num_r_index = i
        num_l_index = i+1

    if s[i] == "L" and s[i+1] == "R":
        # print(num_r_index)
        # print(num_l_index)
        # print(num_r)
        # print(num_l)
        # print()
        right = (num_r+1)//2 + (num_l)//2
        left = (num_r)//2 + (num_l+1)//2
        ans[num_r_index] = right
        ans[num_l_index] = left
        num_r = 0
        num_l = 0

num_l += 1
right = (num_r+1)//2 + (num_l)//2
left = (num_r)//2 + (num_l+1)//2
ans[num_r_index] = right
ans[num_l_index] = left
num_r = 0
num_l = 0

# print(ans)
for i in ans:
    print(i, "", end="")
print()
