from art import logo
print(logo)
print("Welcome to the secret auction program.")

# TODO-4: Compare bids in dictionary
def find_highest_bid(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid of ${highest_bid}")


# TODO-2: Save data into dictionary {name: price}
bids = {}

continue_bidding = True
# TODO-3: Whether if new bids need to be added
while continue_bidding:
# TODO-1: Ask the user for input
    name = input("What is your name ? ")
    price = int(input("What's your bid ? : $"))
    bids[name] = price
    should_continue = input("Are there any other bidders ?  type 'yes' or 'no'.\n").lower()
    if should_continue == 'no':
        continue_bidding = False
        find_highest_bid(bids)
    elif should_continue == 'yes':
        print("\n" *20)









