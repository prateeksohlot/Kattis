import sys

data_all = int(input())

num_months= int(input())

remain_data = data_all

for id,mb in enumerate(sys.stdin):
    if id>=0:
        data = mb
        # print(data)
        temp = remain_data - int(data)
        remain_data = temp+data_all
        # print(remain_data)
    if id==num_months-1:
        break

print(remain_data)

