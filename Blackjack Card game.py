import random
#blackjack card game
#create a deck of cards
def create_deck(): 
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck


# show user hands
dealer_hand = []
player_hand = [] 

#deal 1  card at a time to player and dealer
def deal_initial_cards(deck, player_hand, dealer_hand):
    for _ in range(2):
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())

# calculate the value of a hand
def calculate_hand_value(hand):
    value = 0
    aces = 0
    for card, _ in hand:
        if card in ['Jack', 'Queen', 'King']:
            value += 10
        elif card == 'Ace':
            aces += 1
            value += 11  # Initially count Ace as 11
        else:
            value += int(card)  # Convert number cards to int
    while value > 21 and aces:
        value -= 10  # Adjust for Aces if value exceeds 21
        aces -= 1
    return value

# display hands
def display_hands(player_hand, dealer_hand, reveal_dealer=False):
    print("\nPlayer's Hand:", player_hand, "Value:", calculate_hand_value(player_hand))
    if reveal_dealer:
        print("Dealer's Hand:", dealer_hand, "Value:", calculate_hand_value(dealer_hand))
    else:
        print("Dealer's Hand: [Hidden]", dealer_hand[1:])  # Show only the second card of dealer's hand

# check for blackjack
def check_blackjack(hand):
    return calculate_hand_value(hand) == 21

# main game loop
def play_blackjack():
    deck = create_deck()
    deal_initial_cards(deck, player_hand, dealer_hand)
    
    display_hands(player_hand, dealer_hand)
    
    if check_blackjack(player_hand):
        print("Blackjack! Player wins!")
        return
    
    while True:
        action = input("Do you want to (h)it or (s)tand? ").lower()
        if action == 'h':
            player_hand.append(deck.pop())
            display_hands(player_hand, dealer_hand)
            if calculate_hand_value(player_hand) > 21:
                print("Player busts! Dealer wins!")
                return
        elif action == 's':
            break
        else:
            print("Invalid input. Please enter 'h' or 's'.")
    
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    
    display_hands(player_hand, dealer_hand, reveal_dealer=True)
    
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    
    if dealer_value > 21 or player_value > dealer_value:
        print("Player wins!")
    elif player_value < dealer_value:
        print("Dealer wins!")
    else:
        print("It's a tie!")
    
# Start the game
if __name__ == "__main__":
    play_blackjack()
# This code implements a simple Blackjack card game where a player can play against a dealer.