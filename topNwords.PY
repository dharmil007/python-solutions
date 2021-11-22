dict_topN = {}
list_topN = []
with open ("lyrics.txt") as file:
    for line in file:
        line = line.strip().lower()
        words = line.split(" ")
        for word in words:
            dict_topN[word] = dict_topN.get(word,0)+1
    
    for (k,v) in dict_topN.items():
        list_topN.append((v,k))
        list_topN.sort(reverse=True)

    count =0
    for li in list_topN:
        if count<21:
            count=count+1
            print (li)
        else:
            break

