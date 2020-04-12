#!/usr/bin/env python3

n, m = map(int, input().split())

flag = 0
ans = [None for i in range(n)]
# print(ans)
for i in range(m):
    s, c = map(int, input().split())
    if ans[s-1] is None or ans[s-1] == c:
        ans[s-1] = c
    else:
        flag = 1
        break

# print(flag)
if n == 1:
    if ans[0] is None:
        ans[0] = 0
    print("".join(map(str, ans)) if flag == 0 else -1)
else:
    if ans[0] == 0:
        flag = 1
    if ans[0] is None:
        ans[0] = 1
    for i in range(1, len(ans)):
        if ans[i] is None:
            ans[i] = 0

    print("".join(map(str, ans)) if flag == 0 else -1)
