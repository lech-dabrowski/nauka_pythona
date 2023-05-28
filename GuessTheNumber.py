import random

print(".: Guess the number game :.")
print()
play_again = True

while play_again:
    count = 0
    number = random.randint(1, 100)

    while True:
        count += 1
        user_guess = int(input("Type in a number between 1 and 100: "))

        if user_guess > number:
            print("Too big. Try again:")
        elif user_guess < number:
            print("Too small. Try again.")
        elif user_guess == number:
            print(f"Bravo! You needed {count} tries!")
            break

    play_again_input = input("Do you want to play again? (y/n): ")
    if play_again_input.lower() != "y":
        play_again = False
        print("Thanks for playing!")
