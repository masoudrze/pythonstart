import random
round=random.randint(0,1)
i=0

def countNum(i,step):
    j=1
    while j <= step:
        if i==21:
            break
        i += 1
        j += 1
        print(f"-{i}-")
    return i

while i < 21:
    if round==0:
        print("Computer turn:\n")
        step=random.randint(1,3)
        i=countNum(i,step)
        round=1
    else:
        print("your turn:\n")
        step=int(input("Enter steps count[1-3]:\n"))
        i=countNum(i,step)
        round=0
if round==0:
    print("you lost the game")
else:
    print("you won the game")


