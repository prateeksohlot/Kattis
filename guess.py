import sys

a = 0
b = 1001


i = 0
while i<10:
    m = int((a+b)/2)
    print(m)
    n = input().strip()
    if n == 'lower':
        b = m
        # print("asd")
    elif n == 'higher':
        a = m
        # print("nsm")
    elif n == 'correct':
        break
    i += 1

    

    
