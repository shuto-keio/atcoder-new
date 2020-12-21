#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

h, w = list(map(int, input().split()))

ans = 10**10

ans = 10**10
# tate
if h >= 3:
    if h % 3 == 0:
        ans_tmp = 0
    else:
        ans_tmp = ((h//3+1) * w)-((h//3) * w)
    ans = min(ans, ans_tmp)

if w >= 3:
    if w % 3 == 0:
        ans_tmp = 0
    else:
        ans_tmp = ((w//3+1) * h)-((w//3) * h)
    ans = min(ans, ans_tmp)

for i in range(1, h):
    h1 = i
    h2 = h-i

    if w % 2 == 0:
        s1 = h1*w
        s2 = h2*(w//2)
        s3 = h2*(w//2)
        ans_tmp = max(abs(s1-s2), abs(s1-s3), abs(s2-s3))
    else:
        s1 = h1*w
        s2 = h2*(w//2+1)
        s3 = h2*(w//2)
        ans_tmp = max(abs(s1-s2), abs(s1-s3), abs(s2-s3))
    ans = min(ans, ans_tmp)

for i in range(1, w):
    w1 = i
    w2 = w-i

    if h % 2 == 0:
        s1 = w1*h
        s2 = w2*(h//2)
        s3 = w2*(h//2)
        ans_tmp = max(abs(s1-s2), abs(s1-s3), abs(s2-s3))
    else:
        s1 = w1*h
        s2 = w2*(h//2+1)
        s3 = w2*(h//2)
        ans_tmp = max(abs(s1-s2), abs(s1-s3), abs(s2-s3))
    ans = min(ans, ans_tmp)

print(ans)
