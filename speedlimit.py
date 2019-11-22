import sys

case1 = int(input())
val = list()

for id,x in enumerate(sys.stdin):
    if id>=0:
        val = list(x.split())
        print(val)
        
    if id== case1 -1:
        break
        



# 3
# 20 2
# 30 6
# 10 7
# 2
# 60 1
# 30 5
# 4
# 15 1
# 25 2
# 30 3
# 10 5
# -1
