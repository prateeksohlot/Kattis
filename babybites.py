import sys

# def compare(x,y):
#     return x==''.join(y)

n = int(input().strip())
count = input().split()
num = []

for i in range(1,n+1):
    num.append(str(i))

for id,x in enumerate(count):
    if "mumble" in x:
        count[id] = str(id+1)

s = (count == num)
# print(s)
if s == True:
     print("makes sense")
else:
    print("something is fishy")
    