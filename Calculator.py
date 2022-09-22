#calculator

def add(n1,n2):
  return n1 + n2

#subtract
def sub(n1, n2):
  return n1 + n2

#multiply 
def mult(n1, n2):
  return n1 * n2

#divide
def div(n1, n2):
  return n1 / n2 

operation = {"+" : add, "-": sub, "*": mult, "/" : div}

more = True

for i in operation:
  print(i)
num1 = int(input("what is the 1st number : "))
while more:
  
  operation_symbol = input("pick an operation: ")
  num = int(input("what is the next number : "))
  calculation_function = operation[operation_symbol]
  ans = calculation_function(num1,num)
  print(f"{num1} {operation_symbol} {num} = {ans}")
  user_permission = input("type yes if you want to do more calcutation and type e to exit : ")
  if user_permission == "yes":
    num1 = ans
  else : 
    more = False
    #calculator

def add(n1,n2):
  return n1 + n2

#subtract
def sub(n1, n2):
  return n1 + n2

#multiply 
def mult(n1, n2):
  return n1 * n2

#divide
def div(n1, n2):
  return n1 / n2 

operation = {"+" : add, "-": sub, "*": mult, "/" : div}


def calculator():
  for i in operation:
    print(i)
  more = True
  num1 = float(input("what is the 1st number : "))
  while more:
    
    operation_symbol = input("pick an operation: ")
    num = float(input("what is the next number : "))
    calculation_function = operation[operation_symbol]
    ans = calculation_function(num1,num)
    print(f"{num1} {operation_symbol} {num} = {ans}")
    user_permission = input("type yes if you want to do more calcutation and type e to exit : ")
    if user_permission == "yes":
      num1 = ans
    else : 
      more = False
      calculator()
calculator()