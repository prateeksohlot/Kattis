import sys
import math
# n = int(input())


for a in sys.stdin:
    if a == '\n':
        break
    n = int(a)
    d = []
    x =0
    for i in range(1,int(math.sqrt(n))+1):
        if (n%i)==0:
            d.append(i)
            x += i

    for j in d:
        if d.count(int(n/j))==0 and int(n/j) != n:
            x += int(n/j)
    
    if x == n:
        print(n,'perfect')
    elif (n+2)>=x>=(n-2):
        print(n, 'almost perfect')
    else:
        print(n, 'not perfect')
    
    
