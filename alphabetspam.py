# white space, lower case, upper case, symbols
# white = 95
# 33 to 64 ,91 to 94,123 to 126
letter = input()

w, l , u , s = 0, 0, 0, 0

for i in letter:
    if ord(i) == 95:
        w +=1

    elif 65 <= ord(i) <= 90:
        l += 1

    elif 97 <= ord(i) <= 122:
        u += 1

    else:
        s += 1

print(w/len(letter))
print(u/len(letter))
print(l/len(letter))
print(s/len(letter))