import sys

n = input().split()
des = list()

for id,p in enumerate(sys.stdin):
    if id>=0:
        des.append(p)

    if id==int(n[0])-1:
        break

print (n[1])
# print (des)

