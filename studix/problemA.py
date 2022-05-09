"""
stack of n coins
numbered fron 1 to n
total no. of coins  = 1000
"""

n = int(input()) # number of stacks
coins = list(map(int, input().split()))

sortedCoins = coins.copy()
sortedCoins.sort(reverse=True)

# whether they can finish the game or not
'''
So we have to form pairs of stacks which form equal numbers
Highest coin should not be greater than sum of ther stacks
if unparied remains we cant finish the game.
'''
seq = []

if (sum(coins)%2 ==0) and (sortedCoins[0] <= sum(sortedCoins[1:])):    
    
    print("yes")
    player1 = 0
    player2 = 0

    # print(sortedCoins)
    while True:
        
        if len(sortedCoins) == 0:
            break
        
        if player1 == 0:
            player1 = sortedCoins.pop(0)
            id = coins.index(player1)
            coins.remove(player1)

        if player2 == 0:
            player2 = sortedCoins.pop(0)
            idx = coins.index(player2)
            coins.remove(player2)

        # print(player1, player2)

        diff = player1 - player2

        
        if diff > 0:
            print("{}, {}\n".format(id+1, idx+1)*player2)
            player1 = diff
            player2 = 0

        elif diff < 0:
            print("{}, {}\n".format(id+1, idx+1)*player1)
            player1 = 0
            player2 = -1*diff

        elif diff == 0:
            print("{}, {}\n".format(id+1, idx+1)*player2)
            player1, player2 = 0,0
            
        
        # while True:
        #     if player1 != 0 and player2!=0:
        #         player1 -= 1
        #         player2 -= 1

        #         seq.append((id+1, idx+1))

        #     else:
        #         break



    # if player1 == 0 and player2 == 0:
    #     print("yes")
    #     # for i, j in seq:
    #     #     print(i,j)
    # else:
    #     print('no')

else:
    print("no")





















