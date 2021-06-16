#random number guessing game
import random

player_points_counter = 0

print("Welcome. The international numberguessing tournament is starting now.")
print("\n")

def print_result():
  global computer_win_counter, player_win_counter
  print (name + " won: " + str(player_win_counter) + " points")

number = random.randint(1,50)
guess = -1

while guess != number:
    guess = int(input("\nGuess a number between 1 and 50: "))
    if guess < number:
      print("Guess a larger number.")
      player_points_counter = player_points_counter - 5

    else:
        print ("Guess a smaller number.")
  
        player_points_counter = player_points_counter - 5
        
print("You guessed the number correctly!")
         