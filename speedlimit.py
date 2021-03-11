import sys

n = int(input())
speed = []
time = []

for id,x in enumerate(sys.stdin):
    if id>=0:
        val = list(x.split())
        speed.append(int(val[0]))
        time.append(int(val[1]))
        
    if id== n-1:
        break

        
dist = 0

for i in range(len(time)):
    if i >=1:
        t = time[i] - time[i-1]
        dist += speed[i] * t

    else:
        dist += speed[i] * time[i]

print(dist,"miles")


# 3
# 20 2
# 30 6
# 10 7
# 2
# 60 1
# 30 5
# 4
# 15 1
# 25 2
# 30 3
# 10 5
# -1
