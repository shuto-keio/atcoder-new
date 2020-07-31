#!/usr/bin/env python3

s = str(int(input()))
k = int(input())


for i in range(k):
    if s[i] != "1":
        print(s[i])
        exit()

print(s[i])

# if s[0] == "1":
#     if k == 1:
#         print(1)
#     else:
#         print(s[1])
# else:
#     print(s[0])
