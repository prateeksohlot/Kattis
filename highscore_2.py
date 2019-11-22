import sys
import math

def eval(a,b,c,d):
    list_abc = [a,b,c]
    (a,b,c) = sorted(list_abc)
    s_1 = (a+d)**2 + b**2 + c**2 + 7*min(a+d,b,c)
    s_2 = a**2 + (b+d)**2 + c**2 + 7*min(a,b+d,c)
    s_3 = a**2 + b**2 + (c+d)**2 + 7*min(a,b,c+d)
    return max(s_1,s_2,s_3)

# def eval_2(a,b,c,d):
#     list_abc = [a,b,c]
#     (a,b,c) = sorted(list_abc)
#     z = math.floor(d/2)
#     y = math.floor(d/2)
#     sc_1 = (a+z)**2 + (b+y)**2 + c**2 + 7*min(a+z,b+y,c)
#     sc_2 = a**2 + (b+z)**2 + (c+y)**2 + 7*min(a,b+z,c+y)
#     sc_3 = (a+z)**2 + b**2 + (c+z)**2 + 7*min(a+z,b,c+z)
#     return max(sc_1,sc_2,sc_3)

n = int(input().strip())
for id,x in enumerate(sys.stdin):
    
    if id>=0:
        x =x.split()
        a = int(x[0])
        b = int(x[1])
        c = int(x[2])
        d = int(x[3])
        score = eval(a,b,c,d)
        score_2 = eval_2(a,b,c,d)
        print (max(score,score_2))
    if id ==n-1:
        break

        