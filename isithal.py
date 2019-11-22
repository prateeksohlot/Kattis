import sys

n = input().split()

if n[0] == 'OCT':
    if int(n[1]) == 31:
        print("yup")
    else:
        print("nope")
elif n[0] == 'DEC':
    if int(n[1]) == 25:
        print("yup")
    else:
        print("nope")
else:
    print("nope")
