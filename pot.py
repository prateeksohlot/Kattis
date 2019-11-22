import sys
import math

n = int(input())

sum = 0
for id,x in enumerate(sys.stdin):
    if id>=0:
        val = list(x.strip('\n')) #strip here is used to convert string to a list
        p = int(val[-1])
        val.pop(-1)
        num = int(''.join(val)) #join is to concatinate all the values in the string
        a = math.pow(num,p)
        sum += a

        # print(*val)
        # num = int(*val) * will print every element of the list with a space 
       
    if id==n-1:
        break
print(int(sum))
# for y in num:
#     print(y)

