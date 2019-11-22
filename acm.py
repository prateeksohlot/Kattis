import sys

time=0
ans = 0
d = []
for i in sys.stdin:
    i = i.split()
    if int(i[0]) == -1:
        break
    d.append(i[1])
    if i[2] == "right" and d.count(i[1]) == 1:
        time += int(i[0])
        ans += 1
        # print(i[0])
    if i[2] == "right" and d.count(i[1]) >1:
        time += int(i[0]) + ((d.count(i[1]) - 1)*20)
        ans += 1
        # print(int(i[0]) + ((d.count(i[1])-1)*20))
        # print(d.count(i[1]))
    # if i[2] == "wrong" :
    #     time += 20
    

# print(d)    
print(ans, time)