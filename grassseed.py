import sys

cost_seed = float(input().strip())
lawns = float(input().strip())

total_cost = 0
for id,x in enumerate(sys.stdin):
    if id>=0:
        x = x.split()
        l = float(x[0])
        b = float(x[1])

        cost_lawn = l*b*cost_seed
        total_cost += cost_lawn

    if id == lawns -1:
        break

print("{0:.8f}".format(total_cost))