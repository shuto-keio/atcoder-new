#!/usr/bin/env python3

x = int(input())

ans = 1
for i in range(2, 32):
    ans_tmp = 1
    while(1):
        # print(ans_tmp**i)
        if (ans_tmp+1)**i <= x:
            ans_tmp += 1

        else:
            break
    ans = max(ans, ans_tmp**i)
print(ans)
