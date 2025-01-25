n=int(input("Enter the number"))
l=int(input("Enter the low number"))
h=int(input("Enter the range number"))
for i in range(l,h+1):
    print(f"{n}X{i}={i*n}")