import random
print("Welcome to number guessing game!")
random_number = random.randint(1,101)
game_type = input("what difficulty level you want to play 'hard' or 'easy' : ").lower()
if game_type =="hard":
  attempts = 5
  while attempts != 0:
    guess = int(input("Guess a number : "))
    if guess == random_number:
      print("You have guessed right, You Win😎")
    elif guess > random_number:
      attempts -= 1
      print("Its too high!")
      print(f"you and {attempts} attempts left ")
    elif guess < random_number:
      attempts -= 1
      print(f"It's too low \n you {attempts} attempts left")
      
elif game_type == "easy":
  attempts = 10
  while attempts != 0 :
    guess = int(input("Guess a number : "))
    if guess == random_number:
      print("You have guessed right, You Win😎")
    elif guess > random_number :
      attempts -= 1
      print(f"It's too high \n you and {attempts} attempts left")
    elif guess < random_number:
      attempts -= 1
      print(f"It's too low \n you and {attempts} attempts left")
  
  