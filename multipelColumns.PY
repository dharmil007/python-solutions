"""
Given a file with multiple columns, print the first and the third column out and find a new value based on the values of those two columns.
"""

with open("multipleC.csv") as file:
    next(file)
    for lineNo,line in enumerate(file):
        line = line.strip()
        words = line.split(",")
        sum1 = 0
        for count,word in enumerate(words[:3]):
            if count==0:
                print("Row:",lineNo,"First Column --> ",word)
                sum1 = sum1+int(word)
            elif count==2:
                print("Row:",lineNo,"Third Column --> ",word)
                sum1 = sum1+int(word)
        print ("Sum of Row:",lineNo,"is --> ",sum1)

