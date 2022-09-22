import random
print("what do you want to choose? type 0 for rock, 1 for paper, and 2 for scissior")

rock = ''' Rock
          _______
      ---'   ____)
            (_____)
            (_____)
    VK      (____)
      ---.__(___)'''

paper = '''Paper
          _______
      ---'   ____)____
                ______)
                _______)
    VK         _______)
      ---.__________)'''

scissors = '''Scissors
          _______
      ---'   ____)____
                ______)
             __________)
    VK      (____)
      ---.__(___)'''

show = int(input("what do you want to choose : "))
if show == 0 :
  print(rock)
elif show ==1 :
  print(paper)
elif show==2 :
  print(scissors)

computer_choice = random.randint(0,2)
print("Computer has choosed : ")
if computer_choice == 0 :
  print(rock)
elif computer_choice ==1 :
  print(paper)
elif computer_choice==2 :
  print(scissors)

if show==0 and computer_choice ==0 :
  print("draw.")
elif show==1 and computer_choice ==1 :
  print("draw")
elif show==2 and computer_choice ==2 :
  print("draw")
elif show==0 and computer_choice ==1 :
  print("you lose")
elif show==0 and computer_choice ==2 :
  print("you win")
elif show==1 and computer_choice ==0 :
  print("you win")
elif show==1 and computer_choice ==2 :
  print("you lose")
elif show==2 and computer_choice ==0 :
  print("you lose")
elif show==2 and computer_choice ==1 :
  print("you win")
