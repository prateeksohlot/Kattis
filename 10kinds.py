import sys
# r = row and c = columns
#binary users = 0 and decimal = 1

row = int(input().split()[0])
something = []

mapping = map(list, something) 

for id, x in enumerate(sys.stdin):
    x = x.split()
    something.append(x)
    
    if id == row-1:
        break