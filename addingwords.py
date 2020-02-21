import time
import sys

# start = time.time()
items = dict()

for id, inp in enumerate(sys.stdin):
    
    x = inp.split()
    
    if 'clear' == x[0]:
        break

    if 'def' == x[0]:
        items[x[1]] = int(x[2])


    if 'calc' == x[0]:

        del x[0], x[-1]
        var = x[::2]
        ops = x[1::2]

        # print(var)
        # print(ops)

        for i in var:
            print(i)
            if i not in items.keys():
                print('Unknown')

            else:
                sum = items[var[0]]

        # print(len(ops))
                for i in range(len(ops)):
                    # print(items[var[i+1]])
                    if i == '+':
                        sum += items[var[i+1]]
                    elif i == '-':
                        sum -= items[var[i+1]]

                    print(sum)
        # for fuck, you in items.items():
        #     if you == sum:
        #         print(inp, fuck)

        #     else:
        #         print('Unknown')       