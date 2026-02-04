# Author: Philip Cullen

# What this program does:
    # 1. Shuffle a new deck
    # 2.Get the deck_id from the response
    # 3. Draw 5 cards
    # 4. Print each card’s value and suit
    # 5. Check for:
        # Pair
        # Three of a kind
        # Straight
        # Flush (all same suit)

import requests
from collections import Counter

# 1. Shuffle a new deck
shuffle_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
shuffle_response = requests.get(shuffle_url).json()

deck_id = shuffle_response["deck_id"]

# 2. Draw 5 cards
draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
draw_response = requests.get(draw_url).json()

cards = draw_response["cards"]

# 3. Print the cards
values = []
suits = []

print("You drew:")
for card in cards:
    print(f"{card['value']} of {card['suit']}")
    values.append(card["value"])
    suits.append(card["suit"])

hand_found = False

value_counts = Counter(values)
suit_counts = Counter(suits)

# Three of a kind
if 3 in value_counts.values():
    print("🎉 Congratulations! You got Three of a Kind!")
    hand_found = True

# Pair
elif 2 in value_counts.values():
    print("🎉 Congratulations! You got a Pair!")
    hand_found = True

# Flush
if 5 in suit_counts.values():
    print("🎉 Congratulations! You got a Flush!")
    hand_found = True

# Straight
value_map = {
    "ACE": 1,
    "2": 2, "3": 3, "4": 4, "5": 5,
    "6": 6, "7": 7, "8": 8, "9": 9,
    "10": 10,
    "JACK": 11,
    "QUEEN": 12,
    "KING": 13
}

numeric_values = sorted(value_map[value] for value in values)

is_straight = True
for i in range(len(numeric_values) - 1):
    if numeric_values[i] + 1 != numeric_values[i + 1]:
        is_straight = False
        break

if is_straight:
    print("🎉 Congratulations! You got a Straight!")
    hand_found = True

# If nothing matched
if not hand_found:
    print("Better luck next time!")

