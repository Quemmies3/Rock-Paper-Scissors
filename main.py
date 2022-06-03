#Import module
import random

# Print multiline instruction
print("\nWinning Rules of the Rock paper scissors game as follows: \n"
            +"Rock vs Paper->Paper wins \n"
            + "Rock vs Scissors->Rock wins \n"
            +"Paper vs Scissors->Scissors wins \n"
            +"If the two players choose the same “character” it's a tie, and the game repeats. \n"
            +"After an invalid character has been played, click enter to continue with the game.\n")

#create a list of play options
p = ["R", "P", "S"]

#set player to False
player = False

while player == False:
#set player to True
    print("\nEnter choice \n R for Rock,  \n P for Paper, or  \n S for Scissors\n")

     # take the input from user
    choice = input("User turn: ")

    # initialize input of choice_name variable
    if choice == "R":
        choice_name = 'Rock'
    elif choice == "P":
        choice_name = 'Paper'
    elif choice == "S":
        choice_name = 'Scissors'
    else:
        print("That's not a valid choice. Check your input and put a valid play!")
        print(input("\nClick enter to continue")) 
        choice = input("User turn: ")
        player = False

        if choice == "R":
            choice_name = 'Rock'
        elif choice == "P":
            choice_name = 'Paper'
        elif choice == "S":
            choice_name = 'Scissors'

    # print user choice
    print("user choice is: " + choice_name)
    print("\nNow its computer turn.......")

    #assign a random play to the computer
    computer_choice = random.choice(p)

    #initialize input of computer_choice_name variable
    if computer_choice== "R":
        computer_choice_name = 'Rock'
    elif computer_choice == "P":
        computer_choice_name = 'Paper'    
    else:
        computer_choice_name = 'Scissors'

    print("Computer choice is: " + computer_choice_name + "\n " )
    print(choice_name + " v/s " + computer_choice_name + "\n")
    
    #conditions for Winnung
    if choice == computer_choice:
        print("Both players selected"  " "+ choice_name +". It's a tie!!" + "Play again " +"\n")
    elif choice == "R":
        if computer_choice == "P":
            print("You lose!", computer_choice_name, "covers", choice_name , end = "\n")
            result = "Paper"
        else:
            print("You win!", choice_name, "smashes", computer_choice_name, end = "\n" )
    elif choice == "P":
        if computer_choice == "S":
            print("You lose!", computer_choice_name, "cut", choice_name)
            result = "Scissors"
        else:
            print("You win!", choice_name, "covers", computer_choice_name)
    elif choice == "S":
        if computer_choice == "R":
            print("You lose...", computer_choice_name, "smashes", choice_name)
            result = "Rock"
        else:
            print("You win!", choice_name, "cut", computer_choice_name)       
    
    print("Do you want to play again? (Y/N)")
    ans = input()

            # if user input n or N then condition is True
    if ans == 'n' or ans == 'N':
            break

print("\nThanks for playing")