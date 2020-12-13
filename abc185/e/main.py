#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))


COST_DEL = 1
COST_INS = 1
COST_SUBST = 1
COST_MATCH = 0


def solve(s, t, flag=False):
    sl = len(s)
    tl = len(t)
    cost = [[0 for i in range(tl+1)] for j in range(sl+1)]
    parent = [[None for i in range(tl+1)] for j in range(sl+1)]
    cost[0][0] = 0
    for i in range(1, sl+1):
        cost[i][0] = cost[i-1][0] + COST_DEL
        parent[i][0] = 'D'
    for i in range(1, tl+1):
        cost[0][i] = cost[0][i-1] + COST_INS
        parent[0][i] = 'I'
    for i in range(1, sl+1):
        for j in range(1, tl+1):
            c_del = cost[i][j-1] + COST_DEL
            c_ins = cost[i-1][j] + COST_INS
            c_subst = cost[i-1][j-1] + COST_SUBST
            if s[i-1] == t[j-1]:
                c_match = cost[i-1][j-1] + COST_MATCH
            else:
                c_match = sys.maxsize
            cost[i][j] = min(c_del, c_ins, c_subst, c_match)
            if (c_del == cost[i][j]):
                if parent[i][j] is None:
                    parent[i][j] = 'D'
                else:
                    parent[i][j] = ('D', parent[i][j])
            if (c_ins == cost[i][j]):
                if parent[i][j] is None:
                    parent[i][j] = 'I'
                else:
                    parent[i][j] = ('I', parent[i][j])
            if (c_subst == cost[i][j]):
                if parent[i][j] is None:
                    parent[i][j] = 'S'
                else:
                    parent[i][j] = ('S', parent[i][j])
            if (c_match == cost[i][j]):
                if parent[i][j] is None:
                    parent[i][j] = 'M'
                else:
                    parent[i][j] = ('M', parent[i][j])
    if flag is True:
        print(cost)
        print(parent)
    return cost[sl][tl]


print(solve(a, b))
