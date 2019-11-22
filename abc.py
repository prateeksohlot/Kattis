import sys

n = input().split()
p = input().strip()
b = []
for i in n:
    b.append(int(i))
b = sorted(b)

op = []
for i in p:
    if i == 'A':
        op.append(b[0])
    elif i == 'B':
        op.append(b[1])
    elif i == 'C':
        op.append(b[2])

print(b)



