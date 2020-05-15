#!/usr/bin/env python3

n = int(input())

sup = n % 2
odd_num = n//2+sup
even_num = n//2

print(odd_num/(even_num+odd_num))
