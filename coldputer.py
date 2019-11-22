import sys

belze = 0
for id,data in enumerate(sys.stdin):
    if id>0:
        temp = data.split()
        for i in temp:
            if int(i)<0:
                belze +=1
    if id>=1:
        print(belze)
        break        

    