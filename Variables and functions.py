import random


def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissor): ")
    options = ["rock", "paper", "scissor"]
    computer_choices = random.choice(options)
    computer_choice = computer_choices
    choices = {"player": player_choice, "computer": computer_choice}
    return choices 

#print(choices)
def check_win(player, computer):
    print(f"You chose {player}, Computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissor":
            return "You are a winner!"
        else:
            return "Paper covers rock. You lose, loser."
    if player == "paper":
        if computer == "rock":
            return "You are a common W."
        else:
            return "Waling L, BOZO"
    elif player == "scissor":
        if computer == "rock":
            return "L bozo, get ratioed"
        else:
            "Free dub"
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)

            
            
        



    
