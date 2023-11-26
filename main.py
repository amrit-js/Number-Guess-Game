import random

def guess_the_number():

    print("Welcome to the Number Guessing Game!")
    lower_limit=int(input("Enter the minimum number:"))
    upper_limit=int(input("Enter the maximum number:"))
    secret_number = random.randint(lower_limit, upper_limit)
    attempts = 0

    while True:
        
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        
        if user_guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif user_guess < secret_number:
            print("The number is low.")
        else:
            print("The numer is high.")

if __name__ == "__main__":
    guess_the_number()
