#Caclulate Fibonacci

n = 25
fib = [0,1,1]

if n==1:
    print(fib[1])
elif n==0:
    print (fib[0])
elif n==2:
    print (fib[2])
else:   
    for i in range(3,n+1):
        fib.append(fib[-2]+fib[-1]+fib[-3])

print (fib[-1])
#print (sum(fib))
    
