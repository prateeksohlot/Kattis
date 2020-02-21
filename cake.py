x = input().split()

h = 4 #Given height of cake
l = int(x[0]) #length of sides
hor = int(x[1]) #horizontal cut
ver = int(x[2])
vol1 = hor*ver*h
vol2 = (l - hor)*ver*h
vol3 = (l - hor)*(l-ver)*h
vol4 = hor*(l-ver)*h

print(max(vol1, vol2, vol3, vol4))




