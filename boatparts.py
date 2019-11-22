import sys

parts = []
no_parts = 0
for id,x in enumerate(sys.stdin):
    x = x.split()
    
    if id==0:
        n = int(x[1])
        no_parts += int(x[0])
    if id>0:
        parts.append(x[0])

    if id == n:
        
        break

indexes = [parts.index(x) for x in set(parts)]
if len(set(parts)) == no_parts:
    print(max(indexes)+1)
else:
    print('paradox avoided')



