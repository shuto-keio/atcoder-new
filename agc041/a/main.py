#!/usr/bin/env python3

n, a, b = list(map(int, input().split()))

ans = 10**18+1

if a > b:
    a, b = b, a

# print(a, b)
ans = []
ans.append(max(a-1, b-1))
ans.append(max(n-a, n-b))

if abs(a-b) % 2 == 0:
    ans.append(abs(a-b)//2)
else:
    a_tmp, b_tmp = 1, b-a
    ans.append(a + abs(b_tmp-a_tmp)//2)

    a_tmp, b_tmp = a+(n-b)+1, n
    ans.append(n-b+1 + abs(b_tmp-a_tmp)//2)
# print(ans)
print(min(ans))
