#!/usr/bin/env python3

n, k = list(map(int, input().split()))
r, s, p = list(map(int, input().split()))
t = list(str(input()))

point = {}
point["r"] = p
point["s"] = r
point["p"] = s

ans = 0
for i in range(k):
    j = 1
    count = 1
    letter = t[0+i]
    # print(letter)
    while(1):
        if j*k+i >= len(t):
            break

        letter_next = t[j*k+i]
        if letter == letter_next:
            count += 1
        else:
            # print((count+1//2)*point[letter])
            # print(count)
            ans += ((count+1)//2)*point[letter]
            count = 1
        letter = letter_next
        # print(letter)
        j += 1
    # print((count+1//2)*point[letter])
    # print(count)
    # print()
    ans += ((count+1)//2)*point[letter]

print(ans)
