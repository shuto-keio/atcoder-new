#!/usr/bin/env python3
from collections import Counter

h, w, m = list(map(int, input().split()))

H = []
W = []
for i in range(m):
    hh, ww = tuple(map(int, input().split()))
    H.append(hh)
    W.append(ww)
h_m = Counter(H).most_common()[0]
w_m = Counter(W).most_common()[0]

ans_1 = h_m[1]
ans_2 = w_m[1]

# print(ans_1, ans_2)
WW = []
HH = []
for i in range(m):
    if H[i] == h_m[0]:
        continue
    WW.append(W[i])

for i in range(m):
    if W[i] == w_m[0]:
        continue
    HH.append(H[i])
if WW:
    ans_1 += Counter(WW).most_common()[0][1]
if HH:
    ans_2 += Counter(HH).most_common()[0][1]

print(max(ans_1, ans_2))


# hw.sort()
# hw_rev = sorted(hw, key=lambda x: x[1])

# index_sum_h = []
# sum_h = []
# index = -1
# for i in hw:
#     a, b = i
#     if a == index:
#         index_sum_h[-1][1] += 1
#     else:
#         index = a
#         index_sum_h.append([a, 1])

# index_sum_w = []
# index = -1
# for i in hw_rev:
#     a, b = i
#     if b == index:
#         index_sum_w[-1][1] += 1
#     else:
#         index = b
#         index_sum_w.append([b, 1])

# # print(hw)
# # print(index_sum_h)
# # print(index_sum_w)

# index_sum_h = sorted(index_sum_h, key=lambda x: x[1], reverse=True)
# index_sum_w = sorted(index_sum_w, key=lambda x: x[1], reverse=True)

# # print(index_sum_h)
# # print(index_sum_w)
# dq = deque([[0, 0]])

# ans_tmp = index_sum_h[0][1]+index_sum_w[0][1]

# hw = set(hw)
# while len(dq) > 0:
#     index_h, index_w = dq.popleft()
#     a, b = index_sum_h[index_h]
#     c, d = index_sum_w[index_w]

#     # print([a, c])
#     # print([a, c] in hw)
#     if (a, c) in hw:
#         ans = ans_tmp-1
#         if index_h+1 < len(index_sum_h):
#             if index_sum_h[index_h+1][1] == b:
#                 dq.append([index_h+1, index_w])
#         if index_w+1 < len(index_sum_w):
#             if index_sum_w[index_w+1][1] == d:
#                 dq.append([index_h, index_w+1])

#     else:
#         print(b+d)
#         exit()

# print(ans)
