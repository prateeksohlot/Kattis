import sys

moves = list(input())

pos = 1

for move in moves:
    if move == "A":
        if pos ==1:
            pos = 2
        elif pos==2:
            pos = 1
    
    if move == "B":
        if pos==2:
            pos = 3
        elif pos==3:
            pos = 2
    if move == "C":
        if pos==3:
            pos = 1
        elif pos ==1:
            pos = 3
   

print(pos)
    

    
