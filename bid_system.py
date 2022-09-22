logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

bid_dis = {}
bid = True
while bid:
  Name = input("what is your name? : \n")
  bid_amount = int(input("How much you want to bid? : \n"))
  bid_dis[Name] = bid_amount
  anyother_bid = input("Anyone left to bid type yes if there is otherwise no").lower()
  if anyother_bid =="no":
    bid = False
high = 0
winner = ""
for Highest_bid in bid_dis:
  amount = bid_dis[Highest_bid]
  if amount > high:
    high = amount
    winner = Highest_bid

print(f"The highest bid is {high} and winner is {winner}")

  