#!/usr/bin/env python3
import itertools

n, m, q = list(map(int, input().split()))

a = []
b = []
c = []
d = []
for i in range(q):
    a_, b_, c_, d_ = list(map(int, input().split()))
    a.append(a_)
    b.append(b_)
    c.append(c_)
    d.append(d_)

ans = 0
for seq in itertools.combinations_with_replacement(range(1, m+1), n):
    ans_tmp = 0
    for i in range(q):
        if seq[b[i]-1]-seq[a[i]-1] == c[i]:
            ans_tmp += d[i]
    ans = max(ans, ans_tmp)
print(ans)
