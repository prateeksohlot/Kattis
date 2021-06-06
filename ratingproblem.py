import sys

#n is no of judges and k is judges who voted
n , k = input().split()

total = []

for id, x in enumerate(sys.stdin):
        
    total.append(int(x))
    
    if id == int(k) - 1:
        break

diff = (int(n) -int(k))

print((sum(total)+ (diff * -3))/int(n) , (sum(total)+ (diff * 3))/int(n))


    
