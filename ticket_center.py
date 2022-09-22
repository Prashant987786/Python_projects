print("Welcome to ticket center")
height = int(input("Enter your height in cm ? : "))
age = int(input("Enter your age? : "))
bill = 0

if height >= 120 :
  if age >= 18 :
    bill = 12
    print("Adult ticket are 12$")
  elif age <=12 :
    bill = 5
    print("Child ticket are 5$")
  else :
    bill = 7
    print("Youth ticket are 7$")

  pic = str(input("Do you want to click picture? Y & N : "))

  if pic == "Y" :
    bill += 3
    
  print(f"Your total bill is ${bill}")
else :
  print("you are not ready to go yet. come back after some time")