celsius=int(input("Enter temperature in celsius"))

def fahrenheit(celsius):
    f=(celsius*1.8)+32
    print(f'Fahrenheit is {f}')

def kelvin(celsius):
    k=celsius+273
    print(f'Kelvin is {k}')

def convert():
    print("1-Fahrenheit\n 2-Kelvin\n")
    choice=int(input("Enter the option"))
    if choice==1:
        fahrenheit(celsius)
    elif choice==2:
        kelvin(celsius)
    else:
        print("Please enter correct option")
convert()