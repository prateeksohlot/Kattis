import sys

n = input().strip()
t = 0
c = 0
g = 0

for i in n:
    if i == 'T':
        t +=1
    elif i == 'C':
        c += 1
    elif i == 'G':
        g += 1

# print(t,c,g)
score = t**2 + c**2 + g**2 

if t ==0 or c ==0 or g == 0:
    print(score)
elif t == c == g:
    print(score + (7*t))
else:
    s = min(t,c,g)
    print(score +(7*s))
