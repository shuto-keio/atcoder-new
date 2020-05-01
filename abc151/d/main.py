#!/usr/bin/env python3

from heapq import heappop, heappush

h, w = list(map(int, input().split()))

map_list = [list(str(input())) for _ in range(h)]

ans = 0
for h1 in range(h):
    for w1 in range(w):
        D = [[False]*w for i in range(h)]
        Q = [(0, (h1, w1))]
        while Q:
            q = heappop(Q)
            qh, qw = q[1][0], q[1][1]
            if qh < 0 or qh >= h or qw < 0 or qw >= w:
                continue
            if map_list[qh][qw] == "#":
                continue
            if D[qh][qw]:
                continue
            D[qh][qw] = True
            ans = max(q[0], ans)
            heappush(Q, (q[0]+1, (qh+1, qw)))
            heappush(Q, (q[0]+1, (qh-1, qw)))
            heappush(Q, (q[0]+1, (qh, qw+1)))
            heappush(Q, (q[0]+1, (qh, qw-1)))
print(ans)
