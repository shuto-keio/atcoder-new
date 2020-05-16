#!/usr/bin/env python3

s = str(input())

weth_list = ["Sunny", "Cloudy", "Rainy"]

tom_index = (weth_list.index(s)+1) % 3

print(weth_list[tom_index])

