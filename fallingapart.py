n = int(input())
size = list(map(int, input().split(' ')))

alice = 0
bob = 0

size.sort(reverse=True)

for i in range(n):
    if i%2 :
        bob += int(size[i])

    else:
        alice += int(size[i]) 

print(alice, bob)