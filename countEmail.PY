"""
Count how many times Email is found.
"""
dict_Email = {}
list_Email = []
with open("mBox.Txt") as file:
    for line in file:
        line = line.strip().lower()
        words = line.split(" ")

        for word in words:
            if "@" in word and "." in word:
                word.strip()
                #dict_Email[word] = dict_Email.get(word,0)+1
                list_Email.append(word)
    
    
    print (list_Email)
    print (len(list_Email))