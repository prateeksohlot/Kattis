n = input()
days = [int(i) for i in input().split()]
x = min(days)


print(days(*x).index())
# print()