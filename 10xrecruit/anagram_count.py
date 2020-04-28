#problem A 10X recruit

import sys

def factorial(number):
    if number == 1:
        return 1
    return number * factorial(number -1)                                    

for word in sys.stdin:
    word = word.split()

    if len(word) == 0 or word == None:
        print(0)

    n = len(word[0])    

    for i in range(n):
        
    unique_word = set(word[0])


    products = 1

    for i in unique_word:
        products *= word[0].count(i)

    #print(products)














        
'''
 d={}
    for j in range(n-i+1):
        subs = ''.join(sorted(s[j:j+i]))
        if subs not in d:
            d[subs]=1
        else:
            d[subs]+=1
        
        res +=d[subs]-1
        
print(res)
'''
