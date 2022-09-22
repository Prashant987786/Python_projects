pizza_size = str(input("how much big pizza you want? S, M or L :"))

#variable which we will use in our program
#small_pizza = 15
#edium_pizza = 20
#large_pizza = 25
#pepperoni = 2 
#cheese = 1
total = 0

if pizza_size == "S" :
  total = 15 
elif pizza_size == "M" :
  total = 20 
else :
  total = 25 

add_pepperoni = str(input("Do you want to add pepperoni? Y or N : "))

if add_pepperoni == "Y" : 
  total += 2

extra_cheese = str(input("Do you want to add cheese? Y or N : "))

if extra_cheese == "Y" :
  total += 1

print(f"Your total bill is {total}")

#if pizza_size == "S" :
 # if add_pepperoni == "Y" :
  #  if extra_cheese == "Y" : 
   #   total = small_pizza + pepperoni + cheese
    #  print(f"You have order a small pizza with extra cheese and pepperoni which will cost you ${total}")
    #else : 
     # total = small_pizza + pepperoni
      #print(f"You have order a small pizza with extra pepperoni which will cost you ${total}")
  #else :
   # total = small_pizza
    #print(f"you have order a small pizza which will cost you ${total}")


#if pizza_size == "M" :
 # if add_pepperoni == "Y" :
  #  if extra_cheese == "Y" : 
   #   total = medium_pizza + pepperoni + cheese
    #  print(f"You have order a medium pizza with extra cheese and pepperoni which will cost you ${total}")
    #else : 
     # total = medium_pizza + pepperoni
      #print(f"You have order a medium pizza with extra pepperoni which will cost you ${total}")
  #else :
   # total = medium_pizza
    #print(f"you have order a medium pizza which will cost you ${total}")



#if pizza_size == "L" :
 # if add_pepperoni == "Y" :
  #  if extra_cheese == "Y" : 
   #   total = large_pizza + pepperoni + cheese
    #  print(f"You have order a large pizza with extra cheese and pepperoni which will cost you ${total}")
    #else : 
     # total = large_pizza + pepperoni
      #print(f"You have order a large pizza with extra pepperoni which will cost you ${total}")
  #else :
   # total = large_pizza
    #print(f"you have order a large pizza which will cost you ${total}")



      