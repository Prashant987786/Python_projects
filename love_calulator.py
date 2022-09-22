print("welcome to love calulator : ")
name1 = str(input("Please enter your name : "))
name2 = str(input("Please enter your partner name : "))

name1 = name1.lower()
name2 = name2.lower()

count_l = name1.count("l")
count_l += name2.count("l")

count_o = name1.count("o")
count_o += name2.count("o")

count_v = name1.count("v")
count_v += name2.count("v")

count_e = name1.count("e")
count_e += name2.count("e")

count_t = name1.count("e")
count_t += name2.count("e")

count_r = name1.count("e")
count_r += name2.count("e")

count_u = name1.count("e")
count_u += name2.count("e")

true = count_t + count_r + count_u + count_e
love = count_l + count_o + count_v + count_e

true = str(true)
love = str(love)

status = true + love

status = int(status)
print(f"{status}%")

if status >= 40 and status <= 50 :
  print(f"Your score is {status}%. you are doing fine with each other.")
elif status >50 :
  print(f"your score is {status}%. you are doing great")
elif status <40 :
  print(f"Your score is {status}%")