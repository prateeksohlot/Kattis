import sys

n = int(input())

for idx, x in enumerate(sys.stdin):
    if idx%2:
        continue
    else:
        print(x)

