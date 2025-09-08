import random
def rock_paper_scissors():
    choices=["Rock","Paper","Scissors"]
    user=input("Enter Rock, Paper, or Scissors: ").capitalize()
    if user not in choices:
        return "Invalid choice! Please choose Rock, Paper, or Scissors."
    computer=random.choice(choices)
    print(f"You chose {user}, Computer chose {computer}")
    if user==computer:
        return "It's a tie!"
    elif (user=="Rock" and computer=="Scissors") or (user=="Paper" and computer=="Rock") or (user=="Scissors" and computer=="Paper"):
        return "You win!"
    else:
        return "Computer wins!"
print(rock_paper_scissors())
