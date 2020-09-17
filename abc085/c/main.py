#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n, y = list(map(int, input().split()))


for i in range(max(n+1, y//10000)):
    y_new = y-10000*i
    n_new = n-i

    if (5000*n_new-y_new) % 4000 == 0:
        x = (5000*n_new-y_new) // 4000

        if n_new-x >= 0 and x >= 0:
            # print(y, i*10000+(n_new-x)*5000+x*1000)
            # print(n, i + n_new-x + x)
            print(i, n_new-x, x)
            exit()


print(-1, -1, -1)
