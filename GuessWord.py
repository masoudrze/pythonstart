import random
words=['shadow','apartment','city','bedroom','chopper','lottery','chance','brindge','doctor','refrigerator','gold','yoga','timeline','landscape','cinema','concert']

word=random.choice(words)
guess=[]
attempt=0
for i in word:
    guess.append('_')
print (*guess)

while '_' in guess:
    char=str(input("guess charachter:\n"))
    attempt +=1
    for i in range(len(word)):
        if char == word[i]:
            guess[i]=char
    print(*guess)
print(f"Congratulation, the word was {word} and you guessed it in {attempt} attempts")
