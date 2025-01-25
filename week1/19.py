n= input("Enter the numbers separated by spaces: ")
n1=n.split()
arr=[]
for i in n1:
    arr.append(int(i))
s=set(arr)
n=len(s)
s=list(s)
s.sort()
if(n<=1):
    print('Second Largest is not possible')
else:
    print(s[-2])