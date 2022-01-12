import sys

for idx, jars in enumerate(sys.stdin):
    sweet, sour = jars.split()

    if int(sweet) == 0 and int(sour) == 0:
        break

    if int(sweet) + int(sour) == 13:
        print("Never speak again.")
        continue

    if int(sour) > int(sweet):
        print("Left beehind.")

    elif int(sweet) > int(sour):
        print("To the convention.")

    elif int(sweet) == int(sour):
        print("Undecided.")
