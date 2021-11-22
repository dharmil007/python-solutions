A = [1,2,1,5]
A=[1]
A = [84,80,27]
A=[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

A = list(A)
new_A = [A[0]]
res_A = []
res = []

for a in A:
    if a>new_A[-1]:
        new_A.append(a)
        if len(res) > 0 and a>res[-1]:
            res.append(a)
    elif a<new_A[-1]:
        if a>new_A[-2] and a<new_A[-1]:
            new_A[-1] = a
            if len(res)>0:
                if a>res[-2] and a<res[-1]:
                        res[-1] = a
        else:
            for m,n in enumerate(new_A):
                if a<n:
                    if len(res) < len(new_A):
                        res = new_A
                    elif a>res[-2] and a<res[-1]:
                        res[-1] = a
                    new_A = new_A[:m]
                    new_A.append(a)
                    break
print (res)




