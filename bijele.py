import sys

p = [1,1,2,2,2,8]
n = input().split()
n = [int(i) for i in n]
d = []
for i,j in zip(p,n):
    d.append(str(i-j))

print(' '.join(d))