def prime(n):
    c=0
    i=2
    while i<=n:
        if n%i==0:
            c+=1
        i+=1
    if(c<2):
        print(n)
l=int(input("Enter the low number"))
h=int(input("Enter the high number"))
for i in range(l,h):
    if prime(i):
        print(i)
    else:
        continue