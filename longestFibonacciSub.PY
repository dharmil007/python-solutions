'''

https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

'''

class Solution:
    def lenLongestFibSubseq(self, arr):

        res = []
        long = []
        for i,a in enumerate(arr):
            res.append(a)
            if len(long) <= len(arr[i+1:]):
                for n in arr[i+1:]:
                    if len(res) >= 2:
                        if n == res[-2]+res[-1]:
                            res.append(n)
                        else:
                            if len(res) >=3:
                                if res[-1] != (res[-2]+res[-3]):
                                    res[-1] = n
                            else:
                                if n > res[-1]+res[-2]:
                                    res[-1] = n
                    elif len(res) < 2:
                        res.append(n)
                if len(long) < len(res):
                    long = res
                res=[]

        return (len(long))


so = Solution()            
print (so.lenLongestFibSubseq([1,2,3,4,5,6,7,8]))
print (so.lenLongestFibSubseq([1,3,7,11,12,14,18]))
print (so.lenLongestFibSubseq([2,4,7,8,9,10,14,15,18,23,32,50]))

            

        