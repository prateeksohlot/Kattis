greet = input()

# Method One
'''
count= 0
for i in greet:
    if i =='e':
        count +=1

print("h"+(2*count)*"e" + "y")
'''

# Method Two

print('h'+ 2*greet.count('e')*'e' +'y')