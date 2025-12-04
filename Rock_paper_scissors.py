computer_choice = "scissors"
user_choice = input("what do you choose among rock, paper and scissors\n")

if computer_choice == user_choice:
    print("it is tie")
if computer_choice == "rock" and user_choice == "paper":
    print("you win")
elif computer_choice == "scissors" and user_choice == "rock":
    print("you win")
elif computer_choice == "paper" and user_choice == "scissors":
        print("you win")
else:
    print("you lose")