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

def getStep(min,max):
    step=int(input(f"Enter steps count[{min}-{max}]:\n"))
    while step < min or step > max:
        step=int(input(f"Enter steps count[{min}-{max}]:\n"))
    return step



while i < 21:
    if round==0:
        print("Computer turn:\n")
        step=random.randint(1,3)
        i=countNum(i,step)
        round=1
    else:
        print("your turn:\n")
        step=getStep(1,3)
        i=countNum(i,step)
        round=0
if round==0:
    print("you lost the game")
else:
    print("you won the game")


