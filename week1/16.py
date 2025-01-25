list=input("Enter numbers")
list1=list.split()
n=[]
for i in list1:
    n.append(int(i))
even=[]
odd=[]
for j in n:
    if j%2==0:
        even.append(j)
    else:
        odd.append(j)
print(f"Even:{even}")
print(f"Odd:{odd}")