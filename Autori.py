import sys
# from fuzzywuzzy import fuzz
n = list()
x = list(input())

n.append(x[0])
for id,e in enumerate(x):
    if e == '-':
        # id = x.index(e)
        n.append(x[id+1])

print(''.join(n))
# '' here is the seperator, join is used when we have to print string from the list
    