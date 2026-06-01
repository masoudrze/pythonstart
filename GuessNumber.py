import random

num=random.randint(1,100)
attempt=1
guess=int(input("I picked a number from 1 to 100, guess my number:\n"))
while guess != num:
    if guess>num:
        guess=int(input("It's too high\nTry again, Guess a number from 1 to 100\n"))
        attempt +=1
    if guess<num:
        guess=int(input("It's too low\nTry again, Guess a number from 1 to 100\n"))
        attempt +=1

    print(f"Congratulation, you guessed the number in {attempt} attempt")