#!/usr/bin/env python3

n, k = list(map(int, input().split()))
p = list(map(lambda x: int(x) - 1, input().split()))
c = list(map(int, input().split()))

best = max(c)
for i in range(n):
    curr = 0
    score = [0]
    start = i
    while p[start] != i:
        start = p[start]
        curr += c[start]
        score.append(curr)
    cycle_score = score[-1] + c[i]
    cycle_len = len(score)

    for j in range(cycle_len):
        if j <= k and j != 0:
            # if j <= k:
            cycles = (k-j)//cycle_len
            thing = score[j] + max(0, cycle_score) * cycles
            best = max(best, thing)
        elif j == 0 and k >= cycle_len:
            thing = cycle_score * k//cycle_len
            best = max(best, thing)
print(best)
