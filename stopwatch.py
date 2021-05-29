import sys

n = 0
t = 0
p = 0
for idx, x in enumerate(sys.stdin):
    x = int(x)
    if idx == 0:
        n = x

        if n % 2 != 0:
            print("still running")
            break
        
        continue

    if idx%2 != 0:
        p = x

    else:
        t += (x - p)

    if idx ==(n):
        print(t)
        break


    
        
