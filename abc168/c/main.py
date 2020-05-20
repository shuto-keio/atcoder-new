#!/usr/bin/env python3
import math

a, b, h, m = list(map(int, input().split()))

deg_h = (h*60+m)/(12*60)*2*math.pi
deg_m = (m/60)*2*math.pi

# print(deg_h/(2*math.pi)*360)
# print(deg_m)
h_x = a*math.sin(deg_h)
h_y = a*math.cos(deg_h)
# print(h_x)
# print(h_y)


m_x = b*math.sin(deg_m)
m_y = b*math.cos(deg_m)
# print(m_x)
# print(m_y)
ans = ((h_x-m_x)**2+(h_y-m_y)**2)**0.5
print(ans)
