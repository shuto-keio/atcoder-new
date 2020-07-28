#!/usr/bin/env python3

x1, y1, x2, y2 = list(map(int, input().split()))

grad_x = x2-x1
grad_y = y2-y1

x3, y3 = x2-grad_y, y2+grad_x

x4, y4 = x3-grad_x, y3-grad_y

print(x3, y3, x4, y4)
