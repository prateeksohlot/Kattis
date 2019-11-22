import sys

n = int(input().strip())
typo = {2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z'],0:[' ']}
words = []

for id,x in enumerate(sys.stdin):
    if id >= 0:
        x = x.strip()
        words.append(x)

    if id == n-1:
        break

for i in words:
    for j in range(len(i)):
        a = i[j]
        print(a)    
