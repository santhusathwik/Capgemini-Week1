n=int(input("Enter Number"))
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

if n<0:
    print("Please enter positive number")
else:
    ans=fact(n)
    print(ans)