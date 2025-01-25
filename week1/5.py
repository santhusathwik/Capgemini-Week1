lists=[]
def add():
    name=input("Enter the item name: ")
    price=int(input('Enter the price: '))
    lists.append([name,price]) 
def view():
    for i in lists:
        print(i)
def total():
    ans=0
    for i in lists:
        ans+=i[1]
    return ans

def exit():
    print("Thank You")
    return None

print("\n1-Add\n2-View\n3-Total\n")
while True:
    choice=int(input("Enter the option"))
    if choice==1:
        add()
    elif choice==2:
        view()
    elif choice==3:
        print(f"Total is {total()}")
    elif choice==4:
        exit()
        break