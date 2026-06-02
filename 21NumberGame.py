import random
round=random.randint(0,1)
i=1
while i <= 21:
    if round==0:
        print("Computer turn:\n")
        j=1
        num=random.randint(1,3)
        while j <= num:
            print(f"-{i}-")
            i += 1
            j += 1
        round=1
    else:
        print("your turn:\n")
        j=1
        num=int(input("Enter steps count[1-3]:\n"))
        if num > 3:
            num=int(input("Hey idiot!!!,Enter steps count[1-3]:\n"))
        else:
            while j <= num:
                print(f"-{i}-")
                i += 1
                j += 1
            round=0
if round==0:
    print("Congratulation, you won the game")
else:
    print("you lost the game idiot!!")

