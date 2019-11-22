x = input()

score_A = 0
score_B = 0

for i in range(0,len(x),2):
    # score_A = 0
    # score_B = 0
    if x[i] == 'A':
        score_A += int(x[i+1])
    if x[i] == 'B':
        score_B += int(x[i+1])
        
if score_A > score_B:
    print("A")
else:
    print("B")