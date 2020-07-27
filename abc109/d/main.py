#!/usr/bin/env python3

h, w = list(map(int, input().split()))
a = [list(map(int, input().split())) for i in range(h)]

reverse = 0
count = 0
print_list = []
for h_ in range(h):
    iter_ = range(w)
    if reverse == 1:
        iter_ = reversed(iter_)
    for w_ in iter_:
        if a[h_][w_] % 2 != 0:
            a[h_][w_] -= 1
            if reverse == 0 and w_ == (w-1):
                ww, hh = w_, h_+1
            elif reverse == 1 and w_ == 0:
                ww, hh = w_, h_+1
            else:
                ww, hh = w_+1, h_

            if hh == h:
                continue
            count += 1
            a[hh][ww] += 1

            print_list.append([h_+1, w_+1, hh+1, ww+1])

print(count)
for i in print_list:
    print(*i)
