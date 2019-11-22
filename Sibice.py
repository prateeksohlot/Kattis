import sys
import math

n = input().split()

a = int(math.sqrt(int(n[1])**2 + int(n[2])**2))
# print('Fuck!!!', a)
d = list()

for id,x in enumerate(sys.stdin):
    if id>=0:
        d.append(x)
    if id==int(n[0])-1:
        break

for ans in d:
    if int(ans)<=a:
        print('DA')
    else:
        print('NE')


