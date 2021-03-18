import sys
dominant = {'A': 11, 'K': 4, 'Q':3, 'J':20, 'T': 10, '9': 14, '8':0, '7':0}
normal = {'A': 11, 'K': 4, 'Q':3, 'J':2, 'T': 10, '9': 0, '8':0, '7':0}
score = 0

for id, x in enumerate(sys.stdin):
    # print(id)
    if id ==0:
        hands, dominant_suit = x.split()

        continue
    if id >= 1:
        if x[1] == dominant_suit:
            score += dominant[x[0]]

        else:
            score += normal[x[0]]

    # print(score)
    if id == 4*int(hands):
        break
print(score)    
