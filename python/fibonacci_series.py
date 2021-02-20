# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

#Fibonacci series 0,1,1,2,3,5,8 so we have 7 terms output

n = int(input("Enter no of terms do you want?"))

n1, n2 = 0, 1

if n <=0:
    print("Enter valid")
    
elif n==1:
    print("Fibonacci series of n terms")
    print(n1)
    
else:
    print("Fibonacci series")
    count=0
    fibo = []
    while count<n:
        fibo.append(n1)
        nth = n1+n2
        n1=n2
        n2=nth
        count+=1
    print(fibo)