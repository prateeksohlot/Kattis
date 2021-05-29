import sys

capacity, stops = input().split()

people = 0  # Number of people inside the train1

# left, enter, stayed
for idx, i in enumerate(sys.stdin):

    i = i.split()

    # To check that no one leaves the train on the first station
    if idx == 0:
        if int(i[0]) != 0:
            print("impossible")
            break

    people += int(i[1])
    people -= int(i[0])

    # to ensure number of people entering does not exceed capacity
    if people > int(capacity) or people < 0:
        print("impossible")
        break

    if people < int(capacity):
        if int(i[2]) != 0 and int(i[1]) == 0:
            print("impossible")
            break

    # We check for iteration qual to number of stops and also check the number of waiting people are zero.
    if idx == (int(stops)-1):
        # total number of people in train should also need to be zero
        if int(i[2]) == 0 and int(i[1]) == 0 and people == 0:
            print("possible")

        else:
            print("impossible")

        break
