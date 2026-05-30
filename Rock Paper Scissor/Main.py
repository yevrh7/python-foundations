import random

print("Winning rules of the Rock paper scissor game as follows: \n")
print("Rock vs Paper -> Paper wins")
print("Rock vs Scissors -> Rock wins")
print("Paper vs Scissors -> Scissors wins")

print("\nEnter choice \n 1 for Rock \n 2 for Paper \n 3 for Scissors \n")
while True:
    choice = int(input("Your turn: "))
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    elif choice == 3:
        choice_name = 'Scissors'
    else:
        print("Invalid input, please try again.")
        continue
    print("Your choice is: " + choice_name)
    print("\nNow it's computer's turn...")
    
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'
    
    print("Computer choice is: " + comp_choice_name)
    
    if choice == comp_choice:
        print("It's a tie!")
    elif (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
        print("Computer wins!")
    else:        print("You win!")
    
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'y' and play_again.lower() != 'yes':
        print("Thanks for playing!")
        break