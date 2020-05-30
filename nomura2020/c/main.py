#!/usr/bin/env python3

n = int(input())
a = list(map(int, input().split()))


# if n == 0:
#     if a[0] == 2:
#         print(3)
#     elif a[0] == 1:
#         print(2)
#     exit()

max_num_list = [0]*(n+1)
max_num_list[0] = 1
next_ = 1
for i in range(1, n+1):
    max_num = next_*2
    next_ = max_num-a[i]
    max_num_list[i] = max_num
# print(max_num_list)

list_ = [0]*(n+1)
ans = 0
before = 0
for i in range(n, -1, -1):
    max_num = max_num_list[i]
    if before > (max_num-a[i])*2:
        print(-1)
        exit()
    if max_num-a[i] <= before:
        num = max_num
    else:
        num = before+a[i]
    list_[i] = num
    before = num
    # print(list_)
list_.reverse()
print(sum(list_))
