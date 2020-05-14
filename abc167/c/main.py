#!/usr/bin/env python3
 
import itertools
import numpy as np
 
n, m, x = list(map(int, input().split()))
 
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
data = np.array(data)
 
# print(data)
ans = 10**6*12
for i in itertools.product([0, 1], repeat=n):
    # print(i)
    data_tmp = np.zeros(m+1, dtype=np.int)
    for index in range(len(i)):
        if i[index] == 0:
            continue
        data_tmp += data[index, :]
 
    if np.all((data_tmp[1:] >= x)):
        ans = min(ans, data_tmp[0])
        # print(data_tmp)
 
if ans == 10**6*12:
    print(-1)
else:
    print(int(ans))