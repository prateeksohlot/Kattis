import sys

hand = input().split()

for i in range(len(hand)):
    x = hand[i][0]
    hand[i] = x

st_hand = [hand.count(j) for j in hand]

print(max(st_hand))
