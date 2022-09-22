print("Welcome to this new game...")
print("Your mission is to find treasure")
FstQ = input("this is an crossroad. where do you want to go \"left\" or \"right\" : ").lower()

if FstQ == "left" :
  print("game over...")
else :
  print("you can go ahead")

print("would you to swim or would you like to wait for boat.")
secondq = input("this is an river. would you like to swim or wait for boat : ").lower()

if secondq == "swim" :
  print("game over")
else :
  print("you can go ahead")

print("which door you want to choose red or white or green")

third = input("type red or white or green : ").lower()

if third == "red" :
  print(" game over")
elif third == "white" :
  print("game over")
else :
  print("You win the game. thanks for playing.")