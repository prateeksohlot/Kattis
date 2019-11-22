import sys

time = input().split()

hh = int(time[0])
mm = int(time[1])

alarm = (hh,mm)

mm -= 45

if mm>0:
    alarm = alarm 
if mm < 0:
    mm += 60
    hh -= 1
    if hh < 0:
        hh += 24 

alarm = (hh, mm)

print(*alarm,sep=' ')
