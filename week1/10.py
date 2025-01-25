amount=int(input("Enter amount"))
n=int(input("Enter Number of People"))
tip=int(input("Enter Tip Percentage"))
amount=amount+((tip/100)*amount)
share=amount/n
print(f"Per person share is{share}")