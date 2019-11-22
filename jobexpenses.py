n = int(input())
expenses = input().split()

e = 0

for i in expenses:
    if int(i)<0:
        e -= int(i)

print(e)
