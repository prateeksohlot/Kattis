import sys

n = input().split()

x = 0
for i in n:
    a = n.count(i)
    if a > 1:
     x += 1

if x >1:
    print("no")
else:
    print("yes")



    
