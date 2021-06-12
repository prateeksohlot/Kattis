import sys

n = int(input()) # no. of cases

beeps = []
abeeps = []

for id, x in enumerate(sys.stdin):
    x = x.split()
    b = int(x[0])
    p = float(x[1])

    bpm = 60 * (int(x[0])/float(x[1]))
    beeps.append(bpm)

    abpm = 60 / (float(x[1])/ int(x[0]))
    abeeps.append(abpm)

    if id == n-1:
        break

print(beeps)
print(abeeps)