import sys

n = input().split()
c =[3 ,2 ,1]
pp = 0
for i,j in zip(n,c):
    pp += int(i)*j

if pp>=8:
    print("Province" +" "+ "or" +" "+ "Gold")
elif 8>pp>=6:
    print("Duchy" +" "+ "or" +" "+ "Gold")
elif 6>pp>=5:
    print("Duchy" +" "+ "or" +" "+ "Silver")
elif 5>pp>=3:
    print("Estate" +" "+ "or" +" "+ "Silver")
elif 3>pp>=2:
    print("Estate" +" "+ "or" +" "+ "Copper")
else:
    print("Copper")

 