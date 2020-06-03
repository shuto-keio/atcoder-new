#!/usr/bin/env python3


# import numpy as np

N, A, B, C = list(map(int, input().split()))
L = [int(input()) for _ in range(N)]


inf = 10**9


def dfs(cur, a, b, c):
    if cur == N:
        return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else inf

    ret0 = dfs(cur + 1, a, b, c)
    ret1 = dfs(cur + 1, a + L[cur], b, c) + 10
    ret2 = dfs(cur + 1, a, b + L[cur], c) + 10
    ret3 = dfs(cur + 1, a, b, c + L[cur]) + 10

    return min(ret0, ret1, ret2, ret3)


print(dfs(0, 0, 0, 0))
# ans = 1000
# for i in itertools.product([0, 1, 2, 3], repeat=n):

#     ans_tmp = 0
#     counter = collections.Counter(i)
#     print(counter)
#     if not((1 in counter) and (2 in counter) and (3 in counter)):
#         continue

#     length = [a, b, c]

#     for index, opt in enumerate(i):
#         if opt != 0:
#             length[opt-1] += L[index]

#     print(length)
#     ans_tmp += (counter[1]-1)*10
#     ans_tmp += (counter[2]-1)*10
#     ans_tmp += (counter[3]-1)*10

#     ans_tmp += abs(a - length[0])
#     ans_tmp += abs(b - length[1])
#     ans_tmp += abs(c - length[2])

#     ans = min(ans, ans_tmp)

# print(ans)
