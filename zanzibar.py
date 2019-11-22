import sys

n = int(input().strip())

for id,x in enumerate(sys.stdin):
    # a = []
    if id>=0:
        x = x.split()
        z = 0
        for i in range(len(x)):
            if (i+1) < len(x):
                a = int(x[i])
                b = int(x[i+1])
                s = b - (2*a)
                if s > 0:
                    z += s
                # print(s)
                # z += s
            else:
                break
        # a.append(x)
        print(z)

    if id == n-1:
        break

   