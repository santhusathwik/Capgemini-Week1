name=input("Enter the student name")
m1=int(input("Enter english marks"))
m2=int(input("Enter maths marks"))
m3=int(input("Enter physics marks"))
m4=int(input("Enter chemistry marks"))
m5=int(input("Enter social marks"))

total=m1+m2+m3+m4+m5
percentage=(total/500)*100
if percentage>85:
    grade='A'
elif percentage>55 and percentage<=85:
    grade='B'
elif percentage>35 and percentage<=55:
    grade='C'
else:
    grade='Fail'
print(f"Total:{total}\nPercentage:{percentage}\nGrade:{grade}")