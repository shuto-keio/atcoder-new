#!/usr/bin/env python3


abcde = [int(input()) for _ in range(5)]

first_digit = []
for i in range(len(abcde)):
    if abcde[i] % 10 == 0:
        first_digit.append(10)
    else:
        first_digit.append(abcde[i] % 10)


ans = sum([((i-1)//10+1)*10 for i in abcde])

ans = ans-10+min(first_digit)
print(ans)
