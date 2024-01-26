import random 

wins = 0
loss = 0

options = ["rock","paper","scissors"]

while (True):
    user_input = input("Type Rock/Paper/Scissors or q to quit: ").lower()
    
    if user_input =='q':
        break
    
    if user_input not in options:
        continue

    computer = random.choice(options)
    print("computer : "+ computer+".")

    if user_input == "rock" and computer == "scissors":
        print("You won!")
        wins += 1

    elif user_input == "paper" and computer == "rock":
        print("You won!")
        wins += 1

    elif user_input == "scissors" and computer == "paper":
        print("You won!")
        wins += 1

    else:
        print("You lost!")
        loss += 1

print("You won", wins, "times.")
print("The computer won", loss, "times.")
print("GoodBye")