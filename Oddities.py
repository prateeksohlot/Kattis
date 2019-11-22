import sys

n = int(input())

for id,x in enumerate(sys.stdin):
    if id >= 0:
        x = int(x.strip())
        if x%2==0:
            print(x,"is even")
        else:
            print(x,"is odd")  
    

    if id == n-1:
        break


      