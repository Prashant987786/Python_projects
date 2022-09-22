print("Prime number checker")

def prime_checker(number):
  is_prime = True
  for i in range(2, number) :
    if number % i == 0 :
      is_prime = False
  if is_prime ==True:
    print("the number is prime number")
  else: 
    print("It's not a prime number")
    
n = int(input("What number do you want to check : "))  
prime_checker(number=n)
