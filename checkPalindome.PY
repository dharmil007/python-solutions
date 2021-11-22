"""
to Check iF String is Palindrome
"""

str = "NiTiN"
str="abxxba"
str = "fiitoppp"
str = "abcfdcba"

str = str.lower()

left=0
right=len(str)-1

while (left<=right):
    if str[left] == str[right]:
        left=left+1
        right=right-1
    else:
        print (False)
        exit(0)
print (True)


