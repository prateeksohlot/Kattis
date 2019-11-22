import sys

total_days = int(input().strip())
temp_days = input().split()
mean_temp = []
fuck = []
suck =[]
for i in range(total_days-2):
    m = int(temp_days[i+2]) +int(temp_days[i+1]) + int(temp_days[i])
    m = m/3
    mean_temp.append(m)
    t = int(temp_days[i+2]) - int(temp_days[i])
    fuck.append(abs(t))
b = [id for id, x in enumerate(fuck) if x == min(fuck)]
for a in b:
    

print(fuck)



