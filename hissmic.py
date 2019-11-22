import sys

c = input()
x = c.find('ss',0,len(c))


if x == -1:
    print("no hiss")
else:
    print("hiss")