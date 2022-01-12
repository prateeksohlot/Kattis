text = input()
word1, word2, word3 = text[0:int(len(text)/3)] , text[int(len(text)/3):2*int(len(text)/3)], text[2*int(len(text)/3): len(text)]

if word1 == word2:
    print(word1)
elif word1 == word3:
    print(word1)
else:
    print(word2)

