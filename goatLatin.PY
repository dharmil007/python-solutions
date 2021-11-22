class Solution:
    def toGoatLatin(self,sentence):
        sentence = sentence.rstrip()
        sen = sentence.split (" ")
        newStr = ""

        for i,s in enumerate(sen):
            if s[0] in ("a","e","i","o","u","A","E","I","O","U"):
                newStr = newStr+s+"ma"+"a"*(i+1)+" "
            else: 
                newStr = newStr+s[1:]+s[0]+"ma"+"a"*(i+1)+" "
        
        newStr = newStr.rstrip()
        return (newStr)

s0 = Solution()
print(s0.toGoatLatin("I speak Goat Latin"))
print(s0.toGoatLatin("The quick brown fox jumped over the lazy dog"))
