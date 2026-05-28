import random
print ("Welcome to the Number Guessing Game!")
print ("You have 7 chances to guess the number correctly.")

low = int(input("Enter the lower bound: "))
high = int(input("Enter the upper bound: "))

num = random.randint(low, high)

chances = 7
gc = 0

while gc < chances:
    gc += 1
    guess = int(input("Enter guess: "))
    
    if guess == num:
        print(f'U got it right! The number is {num}.')
        break
    
    elif guess < num:
        print("Ur guess is lower")
        
    elif guess > num:
        print("Ur guess is higher")
        
    if gc >= chances:
        print(f'U ran out of guesses. The right number is {num}')
        break