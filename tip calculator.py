print("welcome to tip calculator")
bill = input("Please enter your bill : ")
bill = int(bill)
tip = input("what percentage of tip do you want to give? 10, 15, 20 : ")
tip = int(tip)
tip_for_10 = bill * .10
tip_for_15 = bill * .15
tip_for_20 = bill * .20
if tip == 10 :
  print("the total tip is : " + str(tip_for_10))
  tip = int(tip_for_10)
elif tip == 15 :
  print("the total tip is : " + str(tip_for_15))
  tip = int(tip_for_15)
elif tip == 20 :
  print("the total tip is : " + str(tip_for_20))
  tip = int(tip_for_20)
else :
  print("you have enter the wrong percentage")

split = input("Do you want to split your bill Yes for 1 and to say No type 0 : ")
if split != 0 : 
  person = input("In how many person you want to split your bill : ")
  person = int(person)
total_bill = (bill / person) + tip
print(" your per person bill is : " + str(total_bill))

