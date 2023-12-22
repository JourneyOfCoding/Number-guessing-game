import random
import time

class GuessNumber:
    def __init__(self, min_range=1, max_range=100):
        # Initialize the game with a random secret number within the specified range
        self.secret_number = random.randint(min_range, max_range)
        self.attempts = 0
        self.given_hint = False
        self.start_time = time.time()
        
    def provide_hint(self):
        if not self.given_hint:
            print(f"Hint: The secret number is between {self.secret_number - 5} to {self.secret_number + 10}.")
            self.given_hint = True
        else:
            print("Oops, sorry! No additional hints are available.")
            
    def play_game(self):
        print("Welcome to the number guessing game.")
        print(f"I am thinking of a number between 1 to 100.")
        
        while True:
            # Get the guessed number from player as input
            guessed_number = self.get_user_input("Guess the number: ")
            self.attempts += 1  # Increment the attempt count
            
            # Provide message based on the guessed number
            if guessed_number < self.secret_number:
                print("Too low! Try again.")
            elif guessed_number > self.secret_number:
                print("Too high! Try again.")
            else:
                taken_time = time.time() - self.start_time
                print(f"Congratulations! You guessed the number in {self.attempts} attempts and {taken_time:.2f} seconds.")
                break
            
            # Provide a hint after 3 attempts
            if self.attempts == 3:
                self.provide_hint()
                
            # Shuffle the secret number after 5 attempts
            if self.attempts == 5:
                print("You have taken 5 attempts. Let me shuffle the secret number.")
                self.secret_number = random.randint(1, 100)
                
    @staticmethod
    def get_user_input(prompt):
        # Ensure the user enters a valid integer as input
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a valid integer number.")
                
# Create an instance of the GuessNumber class with a specified range and start the game
game = GuessNumber(min_range=1, max_range=100)
game.play_game()
