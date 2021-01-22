#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = int(input())

t_num, a_num = list(map(int, input().split()))
for i in range(1, n):
    t, a = list(map(int, input().split()))

    if t_num % t == 0:
        multi_t = t_num//t
    else:
        multi_t = t_num//t+1
    if a_num % a == 0:
        multi_a = a_num//a
    else:
        multi_a = a_num//a+1
    multi = max(multi_t, multi_a)

    t_num_tmp, a_num_tmp = t*multi, a*multi

    # if t_num_tmp == t_num and a_num_tmp == a_num:
    #     t_num_tmp += t
    #     a_num_tmp += a

    t_num, a_num = t_num_tmp, a_num_tmp

    # print(t_num, a_num)
print(t_num+a_num)
