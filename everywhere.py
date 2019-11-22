import sys

n = int(input().strip())

b = []
for i in range(n):
    a = int(input().strip())
    b = []
    for id,x in enumerate(sys.stdin):
        if id >=0:
            x = x.strip()
            b.append(x)

        if id == a-1:
            break
    s = set(b)
    print(len(s))
  