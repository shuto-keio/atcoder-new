#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

sx, sy, tx, ty = list(map(int, input().split()))

ans = []

ans.append("U"*(ty-sy))
ans.append("R"*(tx-sx))


ans.append("D"*(ty-sy))
ans.append("L"*(tx-sx))

ans.append("L"*1)
ans.append("U"*(ty-sy + 1))
ans.append("R"*(tx-sx + 1))
ans.append("D"*1)

ans.append("R"*1)
ans.append("D"*(ty-sy + 1))
ans.append("L"*(tx-sx + 1))
ans.append("U"*1)

print("".join(ans))
