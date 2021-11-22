
#Split Aray in such a way that thier sum is same.
a = [1,4,5,2,3,4,1]
arr1=[]
arr2=[]
sum1=0
sum2=0

for k,i in enumerate(a):
    sum1 = sum1+i
    sum2 = sum(a[k+1:])

    if sum1==sum2:
        arr1 = a[:k+1]
        arr2 = a[k+1:]

if not arr1:
    print (False)
else:
    print (arr1,arr2)
    print (True)