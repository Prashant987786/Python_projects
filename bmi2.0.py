print("Welcome to ticket center")
height = float(input("Enter your height in Meter? : "))
weight = int(input("Enter your weight? : "))

bmi = weight / height ** 2
bmi = float(bmi)

if bmi <= 18 :
  print("You are under weight dear start eating.")
elif bmi <= 25 :
  print("You are normal weight be happy")
elif bmi <= 30 :
  print("you are over weight dear start doing workout")
elif bmi <= 35 :
  print("you are obse....silence...")
else : 
  print("you have enter wrong details or you are fat as hell.")


  