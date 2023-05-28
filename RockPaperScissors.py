from getpass import getpass

valid_choices = ["R", "P", "S", "r", "p", "s"]
winning_combinations = [("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")]

def get_player_choice(player):
    while True:
        choice = getpass(f"Player {player}, please enter R for rock, P for paper, or S for scissors: ")
        if choice in valid_choices:
            return choice.lower()

def determine_winner(player_1_choice, player_2_choice):
    if player_1_choice == player_2_choice:
        return "It's a tie!"
    elif (player_1_choice, player_2_choice) in winning_combinations:
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

player_1_choice = get_player_choice(1)
player_2_choice = get_player_choice(2)

player_1_choice = "rock" if player_1_choice == "r" else "paper" if player_1_choice == "p" else "scissors"
player_2_choice = "rock" if player_2_choice == "r" else "paper" if player_2_choice == "p" else "scissors"

print(determine_winner(player_1_choice, player_2_choice))
