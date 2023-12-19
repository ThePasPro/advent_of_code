# https://adventofcode.com/2023/day/7

card_value = {"T": "A", "J": "B", "Q": "C", "K": "D", "A": "E"}

def determine_card_type(hand): 
    card_value = [hand.count(card) for card in hand]

    if 5 in card_value:
        return 6
    if 4 in card_value: 
        return 5
    if 3 in card_value:
        if 2 in card_value:
            return 4
        return 3
    if card_value.count(2) == 4:
        return 2
    if 2 in card_value:
        return 1
    return 0

def determine_card_value(hand):
    print(hand, (determine_card_type(hand), [card_value.get(card, card) for card in hand]))
    return (determine_card_type(hand), [card_value.get(card, card) for card in hand])

plays = []
for line in open('day_07_input.txt'):
    hand, bid = line.split()
    plays.append((hand, int(bid)))

plays.sort(key=lambda play: determine_card_value(play[0]))
print(plays)
solution = 0
for rank, (hand, bid) in enumerate(plays, 1): 
    solution += rank * bid

print(f'Solution: {solution}')