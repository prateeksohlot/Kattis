import sys
n = int(input())

# K = no. of power strips
# Each strip has 2 to 10 slots

for id, x in enumerate(sys.stdin):
    x = x.split()
    # The last strip will have all slots available for the appliances
    k = x[0]
    x.pop(0)

    op = 0 
    for i in range(len(x)):
        if i < (len(x) - 1):
            op += (int(x[i]) -1)

        elif i == (len(x) - 1):
            op += int(x[i])

    print(op)

    if id == n-1:
        break