import sys
import math

n = int(input().strip())
last_dig = []

for id,x in enumerate(sys.stdin):
    if id>=0:
        f = math.factorial(int(x))
        last_dig.append(str(f%10))

    if id == n-1:
        break

print("\n".join(last_dig))