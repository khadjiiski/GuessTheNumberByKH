import random

computer_number = random.randint(1, 100)
attempts = 0

print("Welcome to the Guess the Number game!")
print("I have selected a number between 1 and 100.")
print("Try to guess it in as few attempts as possible!")
print("Type 'exit' to quit the game at any time.")
print("Type 'reset' to reset the game at any time.")
print("Good luck!")

while True:
    user_input = input("Enter your guess: ")
    
    if user_input.lower() == "exit":
        print("Thanks for playing!")
        break
    elif user_input.lower() == "reset":
        computer_number = random.randint(1, 100)
        attempts = 0
        print("Game has been reset!")
        continue
    
    try:
        guess = int(user_input)
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    attempts += 1
    
    if guess < computer_number:
        print("Too low! Try again.")
    elif guess > computer_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {computer_number} in {attempts} attempts.")
        break