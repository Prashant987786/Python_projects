import random
name_string = input("Give me everybody's names, seperated by a comma. : ")
names = name_string.split(",")

i = len(names)

r = random.randint(0,i -1)
print(f"this person is going to pay the bill is : {names[r]}")