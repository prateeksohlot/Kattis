ques_list = input().split(';')

n = 0

for i in ques_list:
    i = i.split('-')
         
    if len(i) == 1:
        n += 1

    if len(i)> 1:
        n += (int(i[1]) +1 - int(i[0]))
        
print(n)
