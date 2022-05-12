import random
print("NUMBER GUESSING GAME")
number=random.randint(1, 9)
chances=0
print("Guess a number(between 1 and 9):")
while chances<5:
    guess=int(input("ENTER YOUR GUESS"))

    if guess==number:
        print("YOU WON!!")
        
    elif guess<number:
        print("YOUR GUESS WAS TOO LOW, GUESS A NUMBER HIGHER THAN",guess)
        
    else:
        print("YOUR GUESS WAS TOO HIGH, GUESS A NUMBER LOWER THAN",guess)
        
    chances=chances+1
   
if chances>5:
    print("YOU LOSE, THE NUMBER IS",number)
       
