import sys
import math

def score_eval(a,b,c,d):
    unsorted_list = [a,b,c]
    a, b, c = sorted(unsorted_list) #a is always the smallest one

    if a == 0 and b ==0 and d>=2:
        score = 1 + 1 + (c+d-2)**2 +7
    elif b ==0 and c ==0 and d>=2:
        score = 1 + 1 + (a+d-2)**2 +7
    elif a ==0 and c == 0 and d>=2:
        score = 1 + 1 + (b+d-2)**2 +7
    else:
        score1 = (a+d)**2 + b**2 + c**2 + 7*min(a+d,b,c)
        score2 = a**2 + (b+d)**2 + c**2 + 7*min(a,b+d,c)
        score3 = a**2 + b**2 + (c+d)**2 + 7*min(a,b,c+d)
        score = max(score1, score2, score3)
    return score

n = int(input()) 

for id,x in enumerate(sys.stdin):
   
    if id >= 0:
        x = x.split()
        a = int(x[0])
        b = int(x[1])
        c = int(x[2])
        d = int(x[3])

        sc = score_eval(a,b,c,d)
        print(sc)

    if id==int(n)-1:
        break