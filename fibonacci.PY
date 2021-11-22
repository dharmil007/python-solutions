#Caclulate Fibonacci

n = 25
fib = [0,1]

if n==1:
    print(fib[1])
elif n==0:
    print (fib[0])
else:   
    for i in range(2,n):
        fib.append(fib[-2]+fib[-1])

#print (fib[-1])
print (sum(fib))
    
