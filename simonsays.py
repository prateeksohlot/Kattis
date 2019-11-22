import sys

n = int(input().strip())
# result =[]
for id,x in enumerate(sys.stdin):
    if id>=0:
        x.strip()
        if "Simon says" in x:
            print(x[11: ])
        # c = x.find('Simon says',0,len(x))
        # if c == -1:
    
        
    if id==n-1:
        break

# print('\n'.join(result))
