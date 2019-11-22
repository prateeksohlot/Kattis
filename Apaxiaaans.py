import sys

long_name = input().strip()
name = []

for alph in long_name:
    if len(name) == 0:
        name.append(alph)

    if name[-1] != alph:
        name.append(alph)

print(''.join(name))


