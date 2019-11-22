import sys

for a in sys.stdin:
    a = a.split()
    if a == []:
        break
    
    if int(a[1])>=int(a[0]):
        print(int(a[1])-int(a[0]))
    else:
        print(int(a[0])-int(a[1]))