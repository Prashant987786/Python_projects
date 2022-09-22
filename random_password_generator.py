import random
print("Welcome to the pypassword Generator!")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

q1 = int(input("How many letters would you like in your password?\n"))
q2 = int(input("How many numbers would you like?\n"))
q3 = int(input("How many symbols would you like?\n"))

password_list = []

for n in range(1, q1+1):
  random_char = random.choice(letters)
  password_list +=random_char

for n in range(1,q2+1):
  random_num = random.choice(numbers)
  password_list +=random_num

for n in range(1,q3+1):
  random_sym = random.choice(symbols)
  password_list +=random_sym

#print(password_list)
random.shuffle(password_list)
#print(password_list)

password = ""
for char in password_list :
  password +=char

print(password)