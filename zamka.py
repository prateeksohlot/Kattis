import sys

l = int(input().strip())
d = int(input().strip())
x = int(input().strip())
n = []

for i in range (l,d+1):
    z = [int(z) for z in list(str(i))]
    if sum(z) ==x:
        n.append(i)
        
print(min(n))
print(max(n))