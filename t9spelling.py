'''
2-abc 3-def 4-ghi 5-jkl 6-mno 7-pqrs 8-tuv 9-wxyz
'''
#lookup table
table = {"a": "2", "b":"22", "c":"222", "d":"3", "e":"33", "f":"333", "g":"4", "h":"44", "i":"444", "j":"5", "k":"55", "l":"555", "m":"6", "n":"66", "o":"666", "p":"7", "q":"77"\
    , "r":"777", "s":"7777", "t":"8", "u":"88", "v":"888", "w":"9", "x":"99", "y":"999", "z": "9999", " ":"0"}




import sys

n = int(input())

for idx, words in enumerate(sys.stdin):
    
    words = words[:-1]
    
    seq = "Case #{}: ".format(idx+1)
    
    for letter in words:
        if seq[-1] != table[letter][0]:
            seq = seq + table[letter]

        else:
            seq = seq + " " + table[letter]  
      
    
    print(seq)
    if idx == n-1:
        
        break

