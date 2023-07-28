nterms= int(input("Number of terms: "))
n1,n2=0,1
count=0

if nterms <= 0:
    print("Enter a positive integer: ")
elif nterms ==1:
    print("Fibonacci series upto", nterms, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nL=n1+n2
        n1=n2
        n2=nL
        count+=1

