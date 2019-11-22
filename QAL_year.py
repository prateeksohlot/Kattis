import sys

N = int(input()) #number of phases in life
life_qal = 0

for id,qal in enumerate(sys.stdin):
    if id>=0:
        data = qal.split()
        # print(data)
        life_qal += float(data[0]) * float(data[1])
        
        # print(life_qal)

    if id==N-1:
        break
        
print('%.3f'%life_qal)

 

