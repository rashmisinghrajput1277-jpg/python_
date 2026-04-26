import random

# Function to roll dice
def roll_dice():
    return random.randint(1, 6)

# Function to play one round
def play_round():
    print("\n Rolling dice...\n")

    player1 = roll_dice()
    player2 = roll_dice()

    print(f" Player 1 rolled: {player1}")
    print(f" Player 2 rolled: {player2}")

    if player1 > player2:
        print(" Player 1 wins!")
    elif player2 > player1:
        print(" Player 2 wins!")
    else:
        print(" It's a tie!")

# Menu function
def show_menu():
    print("\n======  Dice Roll Game ======")
    print("1. Play Game")
    print("2. Exit")
    print("==============================")

# Main function
def main():
    while True:
        show_menu()
        
        choice = input(" Enter your choice (1 or 2): ").strip()

        if choice == '1':
            play_round()
        elif choice == '2':
            print("\n Thank you for playing! Goodbye!")
            break
        else:
            print(" Invalid choice! Please enter 1 or 2.")

# Run the program
if __name__ == "__main__":
    main()

