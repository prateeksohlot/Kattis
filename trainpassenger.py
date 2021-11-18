import sys

capacity, stops = input().split()

possible = True 

people = 0  # Number of people inside the train1

# left, enter, stayed
for idx, i in enumerate(sys.stdin):

    i = i.split()
    
    # To check that no one leaves the train on the first station
    if idx == 0:
        if int(i[0]) != 0:
            print("impossible")

    #adding people entering the train and leaving the train
    people += (int(i[1]) - int(i[0]))
    
    # Number of people in the train cannot exceed capacity
    if people > capacity:
        print("impossible")

    
    

    # We check for iteration qual to number of stops and also check the number of waiting people are zero.
    if idx == (int(stops)-1) :
        # total number of people in train should also need to be zero and no one enters the train at the last stop
        if int(i[1]) > 0 or int(i[2]) > 0 or people > 0:
            print("impossible")

        else:
            print("possible")

        break
