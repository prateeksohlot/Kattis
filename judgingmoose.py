import sys

n = input().split()

if int(n[0]) == int(n[1]) != 0:
    print("Even",int(n[0]) + int(n[1]))
elif int(n[0]) ==0 and int(n[1])==0:
    print("Not a moose")
else:
    print("Odd",2*max(int(n[0]),int(n[1])))
