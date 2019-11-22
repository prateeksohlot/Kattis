import sys

x  = []
y = []
point = ['','']
for id,i in enumerate(sys.stdin):
    if id>=0:
        c = i.split()
        # print(c[1])
        x.append(c[0])
        y.append(c[1])


    if id==2:
        break
x = sorted(x)
y = sorted(y)

if x.count(x[0]) == 1:
    point[0] = x[0]
else:
    point[0] = x[2]

if y.count(y[0]) == 1:
    point[1] = y[0]
else:
    point[1] = y[2]
    

print(' '.join(point))