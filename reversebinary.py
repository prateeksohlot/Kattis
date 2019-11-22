import sys

n = int(input().strip())

b = bin(n)
b = b[2:]

i = b[::-1]
i = int(i,2)

print(i)