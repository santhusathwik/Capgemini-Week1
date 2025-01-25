def leap(n):
    if n%4==0:
        if n%100==0:
            if n%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
n=int(input("Enter Year"))
if leap(n):
    print(f"{n} is a leap year")
else:
    print(f"{n} is not a leap year")
