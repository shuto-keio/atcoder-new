#!/usr/bin/env python3
import math

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

index = a.index(1)

pre = index
post = n-index-1

ans = 10**10
for i in range(0, k):
    ans_tmp = 0
    pre_tmp = max(0, pre-i)
    post_tmp = max(0, post-(k-1-i))
    ans_tmp += math.ceil(pre_tmp/(k-1))
    ans_tmp += math.ceil(post_tmp/(k-1))
    ans = min(ans, ans_tmp)
    # print(pre_tmp, post_tmp, ans)

print(ans+1)
