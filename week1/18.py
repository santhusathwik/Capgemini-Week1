height=int(input("Enter Height"))
weight=int(input("Enter Weight"))
bmi=weight/height**2
if bmi<18.5:
    print("Underweight")
elif bmi<24.0 and bmi>=18.5:
    print("Normal")
elif bmi>=24.0 and bmi<29.9:
    print("Overweight")
else:
    print("Obese")