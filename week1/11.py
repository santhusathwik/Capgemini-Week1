sp="!@#$%^&*()"
pass1=input("Enter password")
if len(pass1)>=8:
        u=l=d=s=0
        for c in pass1:
            if c>='A'and c<='Z':
                u=1
            if c>='a' and c<='z':
                l=1
            if c>='0' and c<='9':
                d=1
            if c in sp:
                s=1
        if u+l+d+s==4:
            print("Password is Strong")
        else:
            print("Password is Weak")
else:
        print("Password is Weak")
