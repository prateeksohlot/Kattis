import sys
import math

dim = (input().split())
h = int(dim[0])
v = math.radians(int(dim[1]))

length = h/math.sin(v)

print(math.ceil(length))