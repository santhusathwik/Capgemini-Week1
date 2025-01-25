salary=int(input("Enter Salary"))
age=int(input("Enter Age"))
credit=int(input("Enter Credit Score"))

if salary<30000:
    print("Loan rejected due to less salary")
elif age<21:
    print("Loan rejected due to underage")
elif credit<75:
    print("Loan rejected due to low credit score")
else:
    print("Loan Accepted")