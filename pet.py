import sys  

score = []
for id,x in enumerate(sys.stdin):
    if id>=0:
        x = x.split()
        sum_x = sum(map(int,x))
        # That'll take each item in the list, convert it to an integer and sum the results.
        score.append(sum_x)
     
    if id==4:
        break   

print(score.index(max(score))+1 , max(score) )       
    
