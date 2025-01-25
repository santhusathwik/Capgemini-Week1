import random
def game():
    num = random.randint(1, 100)
    c=1
    while c==1:
        n = int(input("Guess the number\n"))
        if n < num:
            print('Too Low\n')
        elif n > num:
            print('Too High\n')
        else:
            print("You got the correct number\n")
            c+=1
game()