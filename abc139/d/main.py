#!/usr/bin/env python3

# import itertools
# n = int(input())

# test_list = list(range(1, n+1))

# ans = 0
# ans_list = []
# ans_score = []
# for i in itertools.permutations(test_list, n):
#     # print(i)
#     ans_tmp = 0
#     for j in range(len(i)):
#         ans_tmp += (j+1) % i[j]
#     ans_score.append(ans_tmp)
#     ans_list.append(i)
#     # print(ans_tmp)

#     ans = max(ans_tmp, ans)

# print("ans:", ans)
# for i in range(len(ans_list)):
#     if ans_score[i] == ans:
#         print(ans_list[i])

n = int(input())

print(((n-1)+1)*(n-1)//2)
