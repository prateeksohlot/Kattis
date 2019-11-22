import sys

status = []
for id,x in enumerate(sys.stdin):
    if id>=0:
        if "FBI" in x:
            status.append(str(id+1))
    
    if id ==4:
        break

if len(status)>0:       
    print(' '.join(status))
else:
    print("HE GOT AWAY!")
