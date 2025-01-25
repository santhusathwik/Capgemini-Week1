str=input("Enter String")
s1=str.lower()
rev=s1[::-1]
if s1==rev:
    print("Palindrome")
else:
    print("Not a Palindrome")