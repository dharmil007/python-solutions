'''
Extract emials and count numbre of Times the email are occuring AND sort it in largest to smallets.
'''
dict_E = {}
with open ("mBox.txt") as file:
    for line in file:
        line = line.lower().strip()
        words = line.split(" ")
        for word in words:
            word = word.strip()
            if "@" in word and "." in word:
                dict_E[word] = dict_E.get(word,0)+1
    file.close()

li = []
for (k,v) in dict_E.items():
    li.append((v,k))
c=0
li.sort(reverse=True)
for l in li:
    if c<30:
        print (l)
        c=c+1
    else:
        break

