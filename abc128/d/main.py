#!/usr/bin/env python3

import heapq

n, k = list(map(int, input().split()))
v = list(map(int, input().split()))

max_try = min(n, k)
ans = 0

for a in range(0, max_try+1):
    for b in range(0, max_try+1-a):
        c = k-(a+b)
        # print(a, b, c, "", end="")
        # print(a, b, c)
        ans_tmp = 0
        garbage = []
        heapq.heapify(garbage)
        for i in range(a):
            num = v[i]
            ans_tmp += num

            if num < 0:
                heapq.heappush(garbage, num)

        for i in range(b):
            num = v[-1-i]
            ans_tmp += num

            if num < 0:
                heapq.heappush(garbage, num)

        # print(garbage)
        for i in range(c):
            # print(garbage)
            if len(garbage) == 0:
                break
            num = -heapq.heappop(garbage)
            # print(num)
            ans_tmp += num
        # print()
        # print(ans_tmp)
        ans = max(ans, ans_tmp)

print(ans)
