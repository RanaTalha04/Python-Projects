import os
from art import logo

print(logo)

bid_store = {}
winner = ""

def storing_bid(Name, Bid):
    bid_store[Name] = Bid

def maximum_bid():
    highest_bid = 0
    winner = ""
    for bidder, bid in bid_store.items():
        if bid > highest_bid:
            highest_bid = bid
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

    
end_bid = True
while end_bid:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    choice = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    storing_bid(Name = name, Bid = bid)
    if choice == 'yes':
        os.system('cls')
    else:
        end_bid = False   
        maximum_bid()
