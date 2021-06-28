# 1< K <= 10 = no. of mailboxes
# 1 < m <= 100 = no. of fire crakers
# 1< N<100 = no. of cases
# a mailbox can fight max 100 firecrackers


import sys

for id, x in enumerate(sys.stdin):
    if id == 0:
        n = int(x)

    x = x.split()

    if int(x[0]) == 1:
        
        print((int(x[1])* (int(x[1]) + 1))/2)


    if id == n:
        break        